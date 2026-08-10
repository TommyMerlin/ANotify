import unittest

import requests

from ANotify._http import DEFAULT_TIMEOUT, HttpTransport, HttpTransportError


class HttpTransportTests(unittest.TestCase):
    def test_uses_default_timeout_and_checks_status(self):
        session = requests.Session()
        transport = HttpTransport(session=session)
        response = requests.Response()
        response.status_code = 200
        response.url = "https://example.test/"

        calls = []

        def request(method, url, **kwargs):
            calls.append((method, url, kwargs))
            return response

        session.request = request
        self.assertIs(transport.get("https://example.test/"), response)
        self.assertEqual(calls[0][2]["timeout"], DEFAULT_TIMEOUT)
        self.assertTrue(session.verify)

    def test_converts_http_error_to_transport_error(self):
        session = requests.Session()
        transport = HttpTransport(session=session)
        response = requests.Response()
        response.status_code = 503
        response.url = "https://example.test/"
        session.request = lambda *args, **kwargs: response

        with self.assertRaises(HttpTransportError):
            transport.post("https://example.test/")

    def test_retries_are_restricted_to_idempotent_methods(self):
        transport = HttpTransport()
        adapter = transport.session.get_adapter("https://")
        retry = adapter.max_retries

        self.assertEqual(retry.total, 3)
        self.assertEqual(set(retry.allowed_methods), {"GET", "HEAD", "OPTIONS"})
        self.assertIn(429, retry.status_forcelist)
        self.assertIn(503, retry.status_forcelist)


if __name__ == "__main__":
    unittest.main()
