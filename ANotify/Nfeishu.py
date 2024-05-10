import os
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

    def send_img(self, receive_id_type: ReceiverType ,receive_id, img_path):
        url = 'https://open.feishu.cn/open-apis/im/v1/messages'

        headers = {
            'Authorization': 'Bearer ' + self.access_token
        }

        params = {
            "receive_id_type": receive_id_type.value
        }

        body = {
            "receive_id": receive_id,
            "msg_type": "image",
            "content": json.dumps({
                "image_key": self.upload_image(img_path)
            })
        }

        res = requests.post(url, params=params, headers=headers, json=body)
        return res.json()

    def send_file(self, receive_id_type: ReceiverType ,receive_id, file_path):
        url = 'https://open.feishu.cn/open-apis/im/v1/messages'

        headers = {
            'Authorization': 'Bearer ' + self.access_token
        }

        params = {
            "receive_id_type": receive_id_type.value
        }

        body = {
            "receive_id": receive_id,
            "msg_type": "file",
            "content": json.dumps({
                "file_key": self.upload_file(file_path)
            })
        }

        res = requests.post(url, params=params, headers=headers, json=body)
        return res.json()

    def upload_image(self, file_path):
        url = "https://open.feishu.cn/open-apis/im/v1/images"

        file_name = os.path.basename(file_path)

        payload = {'image_type': 'message'}
        files = [
            ('image', (file_name, open(file_path, 'rb'), 'application/json'))
        ]
        headers = {
            'Authorization': 'Bearer ' + self.access_token
        }

        response = requests.request("POST", url, headers=headers, data=payload, files=files).json()
        if response['msg'] == 'success':
            return response['data']['image_key']

    def upload_file(self, file_path):
        url = "https://open.feishu.cn/open-apis/im/v1/files"
        file_name = os.path.basename(file_path)

        payload = {
            'file_type': 'stream',
            'file_name': file_name
        }

        files = [
            ('file', (file_name, open(file_path, 'rb'), 'application/json'))
        ]

        headers = {
            'Authorization': 'Bearer ' + self.access_token
        }

        response = requests.request("POST", url, headers=headers, data=payload, files=files).json()
        if response['msg'] == 'success':
            return response['data']['file_key']

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
    # print(feishu.send_file(ReceiverType.OPEN_ID, OPEN_ID, "test.png"))
    # print(feishu.send_msg(ReceiverType.OPEN_ID, OPEN_ID, "Hello World!"))
    # print(feishu.send_msg(ReceiverType.UINION_ID, UNION_ID, "Hello World!"))
    # print(feishu.send_msg(ReceiverType.USER_ID, USER_ID, "Hello World!"))
    # print(feishu.send_msg(ReceiverType.CHAT_ID, CHAT_ID, "Hello World!"))

    # feishu_webhook = FeishuWebhookNotify(webhook_url="https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxxxxxxx")
    # feishu_webhook.send_msg("Hello World!")
