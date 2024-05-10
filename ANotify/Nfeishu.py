import requests
from enum import Enum
import json


class ReceiverType(Enum):
    OPEN_ID = 'open_id'
    CHAT_ID = 'chat_id'
    USER_ID = 'user_id'
    UINION_ID = 'union_id'

class FeishuNotify:
    def __init__(self, appid, appsecret):

        self.appid = appid
        self.appsecret = appsecret
        self.access_token = self.__get_access_token(appid, appsecret)

    # 获取 access_token
    def __get_access_token(self, appid, appsecret):
        url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal'
        params = {
            'app_id': appid,
            'app_secret': appsecret
        }
        resp = requests.post(url, params=params)
        resp.raise_for_status()
        resp_json = resp.json()
        if 'tenant_access_token' in resp_json.keys():
            return resp_json['tenant_access_token']
        else:
            raise Exception('Please check if appid and appsecret are correct \n' + resp.text)

    def send_msg(self, receive_id_type: ReceiverType ,receive_id, msg):
        url = 'https://open.feishu.cn/open-apis/im/v1/messages'

        headers = {
            'Authorization': 'Bearer ' + self.access_token
        }

        params = {
            "receive_id_type": receive_id_type.value
        }

        body = {
            "receive_id": receive_id,
            "msg_type": "text",
            "content": json.dumps({
                "text": msg
            })
        }

        res = requests.post(url, params=params, headers=headers, json=body)
        return res.json()


class FeishuWebhookNotify:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_msg(self, msg):
        url = self.webhook_url
        headers = {
            'Content-Type': 'application/json'
        }
        body = {
            "msg_type": "text",
            "content": {
                "text": msg
            }
        }
        res = requests.post(url, headers=headers, json=body)
        return res.json()

if __name__ == "__main__":
    APPID = ''
    APPSECRET = ''
    OPEN_ID = ''
    UNION_ID = ''
    USER_ID = ''
    CHAT_ID = ''

    feishu = FeishuNotify(appid=APPID, appsecret=APPSECRET)
    # print(feishu.send_msg(ReceiverType.OPEN_ID, OPEN_ID, "Hello World!"))
    # print(feishu.send_msg(ReceiverType.UINION_ID, UNION_ID, "Hello World!"))
    # print(feishu.send_msg(ReceiverType.USER_ID, USER_ID, "Hello World!"))
    # print(feishu.send_msg(ReceiverType.CHAT_ID, CHAT_ID, "Hello World!"))

    feishu_webhook = FeishuWebhookNotify(webhook_url="https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxxxxxxx")
    feishu_webhook.send_msg("Hello World!")
