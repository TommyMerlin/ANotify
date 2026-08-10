from enum import Enum

from ._http import http_transport
from ._result import delivery_result

class MessageType(Enum):
    plaintext = 'text/plain'        # 默认模板，纯文本展
    markdown = 'text/markdown'      # 内容基于markdown格式展示

class GotifyNotify:
    def __init__(self, server_url, token):
        self.server_url = server_url
        self.token = token

    def send_msg(self, title, content, message_type=MessageType.plaintext):
        url = self.server_url.rstrip('/') + "/message"

        querystring = {"token":self.token}

        payload = {
            "extras": { 
                "client::display": { 
                    "contentType": message_type.value 
                    }
                },
            "message": content,
            "priority": 5,
            "title": title
        }
        headers = {"content-type": "application/json"}

        response = http_transport.post(url, json=payload, headers=headers, params=querystring)

        return delivery_result("gotify", response)


if __name__ == "__main__":
    TOKEN = ""
    URL = ""
    gotify = GotifyNotify(URL,TOKEN)
    print(gotify.send_msg("title", "content"))
