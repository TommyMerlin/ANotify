import requests
import json

class WpushNotify:
    def __init__(self, token):
        self.token = token

    """
     * https://docs.wpush.cn/docs/api/message.html
     * @param title
     * @param content
     * @param channel: wechat	是	微信公众号模板消息
                       webhook	是	自定义的webhook地址
                       feishu	是	飞书机器人消息
                       dingtalk	是	钉钉机器人消息
                       wechat_work	是	企业微信机器人消息
                       mail	否	邮件消息，一封邮件消耗0.3个积分
                       sms	否	短信消息，一条短信消耗5个积分
     * @return
    """
    def send_msg(self, title, content, channel = "wechat"):
        url = "https://api.wpush.cn/api/v1/send"

        payload = json.dumps({
            "apikey": self.token,
            "title": title,
            "content": content,
            "channel": channel
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.text


if __name__ == "__main__":
    TOKEN = ""
    wpush = WpushNotify(TOKEN)
    print(wpush.send_msg("title", "content"))