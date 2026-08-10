"""Shared, safe HTTP transport used by synchronous notification clients."""

import logging

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from ._result import TransportError


DEFAULT_TIMEOUT = (3.05, 10)
_RETRYABLE_METHODS = frozenset(("GET", "HEAD", "OPTIONS"))
_RETRYABLE_STATUS_CODES = (429, 500, 502, 503, 504)


class HttpTransportError(TransportError, requests.RequestException):
    """Raised when a request cannot be completed successfully."""


class HttpTransport:
    """A reusable requests transport with bounded requests and safe retries.

    Notification sends are usually POST requests and may have side effects, so
    they deliberately are not retried automatically.  Retries are limited to
    idempotent methods, transient connection/read failures, and 429/5xx
    responses.
    """

    def __init__(self, timeout=DEFAULT_TIMEOUT, session=None):
        self.timeout = timeout
        self.session = session or requests.Session()
        self.session.verify = True
        retry = Retry(
            total=3,
            connect=3,
            read=3,
            status=3,
            backoff_factor=0.5,
            status_forcelist=_RETRYABLE_STATUS_CODES,
            allowed_methods=_RETRYABLE_METHODS,
            respect_retry_after_header=True,
            raise_on_status=False,
        )
        adapter = HTTPAdapter(max_retries=retry, pool_connections=10, pool_maxsize=10)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)
        self._logger = logging.getLogger(__name__)

    def request(self, method, url, **kwargs):
        kwargs.setdefault("timeout", self.timeout)
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response
        except requests.RequestException as exc:
            self._logger.warning("HTTP %s request to %s failed: %s", method.upper(), url, exc)
            raise HttpTransportError("http", "HTTP %s request to %s failed: %s" % (method.upper(), url, exc),
                                     status_code=getattr(getattr(exc, "response", None), "status_code", None)) from exc

    def get(self, url, **kwargs):
        return self.request("GET", url, **kwargs)

    def post(self, url, **kwargs):
        return self.request("POST", url, **kwargs)


# One package-wide transport shares pooled HTTP connections and policy.
http_transport = HttpTransport()
