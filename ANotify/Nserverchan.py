import requests
import json

class ServerChanNotify:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://sctapi.ftqq.com/{token}.send'

    # https://sct.ftqq.com/sendkey
    def send_msg(self, msg_title, msg_text):
        """发送消息
        :msg_title: 主题
        :msg_text:  正文
        :return:    发送是否成功
        """
        data = {
            "text": msg_title,
            "desp": msg_text,
        }

        response = requests.post(self.base_url, data=data)
        response.raise_for_status()
        return response.json()

if __name__ == "__main__":
    TOKEN = ''
    print(ServerChanNotify(TOKEN).send_msg("测试标题", "测试正文"))

