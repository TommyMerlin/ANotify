from ._http import http_transport
from ._result import delivery_result

class BemfaNotify:
    def __init__(self, token):
        self.token = token

    def send_msg(self, title, content):
        url = f"https://apis.bemfa.com/vb/wechat/v1/wechatWarnJson"

        payload = {
            "uid": self.token,
            "device": title,
            "message": content
        }
        headers = {"content-type": "application/json"}

        response = http_transport.post(url, json=payload, headers=headers)

        return delivery_result("bemfa", response)


if __name__ == "__main__":
    TOKEN = ""
    bemfa = BemfaNotify(TOKEN)
    print(bemfa.send_msg("title", "content"))
