import unittest

import requests

from ANotify import DeliveryResult, ProviderError
from ANotify._result import delivery_result


def response(status_code=200, body="", content_type="application/json"):
    result = requests.Response()
    result.status_code = status_code
    result.url = "https://example.test/"
    result.headers["Content-Type"] = content_type
    result._content = body.encode("utf-8")
    return result


class DeliveryResultTests(unittest.TestCase):
    def test_json_response_is_wrapped_in_stable_result(self):
        result = delivery_result("telegram", response(body='{"ok": true, "result": {"message_id": 42}}'))

        self.assertIsInstance(result, DeliveryResult)
        self.assertTrue(result.accepted)
        self.assertEqual(result.channel, "telegram")
        self.assertEqual(result.raw, {"ok": True, "result": {"message_id": 42}})

    def test_text_response_is_wrapped_in_stable_result(self):
        result = delivery_result("telegram", response(body="OK", content_type="text/plain"))

        self.assertIsInstance(result, DeliveryResult)
        self.assertEqual(result.raw, "OK")

    def test_provider_error_is_channel_aware(self):
        with self.assertRaises(ProviderError) as caught:
            delivery_result("wecom", response(body='{"errcode": 40001, "errmsg": "invalid credential"}'))

        self.assertEqual(caught.exception.channel, "wecom")
        self.assertEqual(caught.exception.status_code, 200)
        self.assertEqual(caught.exception.response["errcode"], 40001)

    def test_feishu_nonzero_code_is_provider_error(self):
        with self.assertRaises(ProviderError):
            delivery_result("feishu", response(body='{"code": 99991663, "msg": "invalid token"}'))


if __name__ == "__main__":
    unittest.main()
