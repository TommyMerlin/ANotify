from ._http import http_transport
from ._result import delivery_result

class AnpushNotify:
    def __init__(self, token):
        self.token = token

    def send_msg(self, title, content, channel):
        url = "https://api.anpush.com/push/" + self.token

        payload = {
            "title": title,
            "content": content,
            "channel": channel
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = http_transport.post(url, headers=headers, data=payload)
        return delivery_result("anpush", response)


if __name__ == "__main__":
    TOKEN = ""
    anpush = AnpushNotify(TOKEN)
    print(anpush.send_msg("title", "content", "28334"))
