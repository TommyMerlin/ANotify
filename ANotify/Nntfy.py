from enum import Enum

from ._http import http_transport
from ._result import delivery_result

class MessageType(Enum):
    plaintext = 'text/plain'        # 默认模板，纯文本展
    markdown = 'text/markdown'      # 内容基于markdown格式展示

class NtfyNotify:
    def __init__(self, topic, server_url = "https://ntfy.sh"):
        self.server_url = server_url
        self.topic = topic

    def send_msg(self, title, msg):
        url = self.server_url.rstrip('/') + "/" + self.topic
        response = http_transport.post(url,
            data=msg.encode("utf-8"),
            headers={ "Title": title })

        return delivery_result("ntfy", response)


if __name__ == "__main__":
    TOPIC = ""
    URL = ""
    ntfy = NtfyNotify(TOPIC, URL)
    print(ntfy.send_msg("title","msg"))
