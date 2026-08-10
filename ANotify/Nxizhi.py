from ._http import http_transport
from ._result import delivery_result

class XizhiNotify:
    def __init__(self, token):
        self.token = token

    def send_msg(self, title, content):
        url = f"https://xizhi.qqoq.net/{self.token}.send"

        payload = {
            "title": title,
            "content": content
        }
        headers = {"content-type": "application/json"}

        response = http_transport.post(url, json=payload, headers=headers)

        return delivery_result("xizhi", response)


if __name__ == "__main__":
    TOKEN = ""
    xizhi = XizhiNotify(TOKEN)
    print(xizhi.send_msg("title", "content"))
