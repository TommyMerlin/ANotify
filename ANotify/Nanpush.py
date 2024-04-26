import requests

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

        response = requests.post(url, headers=headers, data=payload)
        return response.text


if __name__ == "__main__":
    TOKEN = ""
    anpush = AnpushNotify(TOKEN)
    print(anpush.send_msg("title", "content", "28334"))