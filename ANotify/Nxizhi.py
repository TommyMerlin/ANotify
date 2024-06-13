import requests

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

        response = requests.post(url, json=payload, headers=headers)

        return response.json()


if __name__ == "__main__":
    TOKEN = ""
    xizhi = XizhiNotify(TOKEN)
    print(xizhi.send_msg("title", "content"))