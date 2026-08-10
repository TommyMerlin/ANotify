"""Common result and error contracts for notification providers."""

from dataclasses import dataclass
from typing import Any, Optional


class NotificationError(Exception):
    """Base exception raised for a notification that was not delivered."""

    def __init__(self, channel, message, *, status_code=None, response=None):
        super().__init__(message)
        self.channel = channel
        self.status_code = status_code
        self.response = response


class TransportError(NotificationError):
    """The HTTP request failed before a provider response was accepted."""


class AuthenticationError(NotificationError):
    """The provider rejected the supplied credentials."""


class ProviderError(NotificationError):
    """The provider returned a successful HTTP response containing an error."""


@dataclass(frozen=True)
class DeliveryResult:
    """A successful notification delivery attempt.

    ``raw`` deliberately preserves the provider response (JSON value or text),
    while the public return type remains stable for every channel.
    """

    channel: str
    accepted: bool
    status_code: Optional[int] = None
    provider_id: Optional[str] = None
    raw: Any = None


def _response_body(response):
    try:
        return response.json()
    except (ValueError, TypeError):
        return response.text


def _provider_error(payload):
    """Return an error message for common provider error envelopes, if any."""
    if not isinstance(payload, dict):
        return None
    if payload.get("ok") is False:
        return payload.get("description") or payload.get("error") or "provider rejected the request"
    if payload.get("errcode", 0) not in (0, None):
        return payload.get("errmsg") or payload.get("msg") or "provider rejected the request"
    code = payload.get("code")
    if isinstance(code, int) and code not in (0, 200, 201, 202):
        return payload.get("message") or payload.get("msg") or payload.get("error") or "provider rejected the request"
    if code == "error" or payload.get("status") == "error":
        return payload.get("message") or payload.get("error") or "provider rejected the request"
    return None


def delivery_result(channel, response):
    """Convert an already status-checked response into a DeliveryResult.

    ``HttpTransport`` raises for non-2xx responses.  This function additionally
    normalizes JSON decoding and turns common provider-level failures into a
    useful, channel-aware exception.
    """
    payload = _response_body(response)
    error = _provider_error(payload)
    if error:
        error_type = AuthenticationError if getattr(response, "status_code", None) in (401, 403) else ProviderError
        raise error_type(channel, str(error), status_code=response.status_code, response=payload)

    provider_id = None
    if isinstance(payload, dict):
        provider_id = payload.get("message_id") or payload.get("messageId") or payload.get("id")
    return DeliveryResult(channel=channel, accepted=True,
                          status_code=getattr(response, "status_code", None),
                          provider_id=str(provider_id) if provider_id is not None else None,
                          raw=payload)


def successful_delivery(channel, *, raw=None, provider_id=None):
    """Create a successful result for transports without an HTTP response."""
    return DeliveryResult(channel=channel, accepted=True, provider_id=provider_id, raw=raw)
