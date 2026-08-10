import os
import json

from ._http import http_transport
from ._result import delivery_result

class DingtalkWebhookNotify:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_msg(self, msg):
        url = self.webhook_url
        headers = {"Content-Type": "application/json"}

        payload = {
            "msgtype": "text",
            "text": {
                "content": msg
            }
        }
        res = http_transport.post(url, data=json.dumps(payload), headers=headers)
        return delivery_result("dingtalk", res)

if __name__ == "__main__":
    webhook_url = ""
    dingtalk = DingtalkWebhookNotify(webhook_url)
    dingtalk.send_msg("Hello World!")

