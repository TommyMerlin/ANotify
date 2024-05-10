import os
import requests
import json

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
        res = requests.post(url, data=json.dumps(payload), headers=headers)
        return res.json()

if __name__ == "__main__":
    webhook_url = ""
    dingtalk = DingtalkWebhookNotify(webhook_url)
    dingtalk.send_msg("Hello World!")

