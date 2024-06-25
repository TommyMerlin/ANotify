import requests

class ChuanxiNotify:
    def __init__(self, token):
        self.token = token

    def send_msg(self, title, content):
        params = {
            'appkey': self.token,
            'title': title,
            'content': content
        }
        resp = requests.get('https://cx.super4.cn/push_msg', params=params)
        return resp.url


if __name__ == "__main__":
    TOKEN = ""
    chuanxi = ChuanxiNotify(TOKEN)
    print(chuanxi.send_msg("title", "content"))