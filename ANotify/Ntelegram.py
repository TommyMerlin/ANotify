import requests
from enum import Enum

# https://core.telegram.org/bots/api#formatting-options
class ParseMode(Enum):
    TEXT = ''
    HTML = 'HTML'
    MarkdownV2 = 'MarkdownV2'
    Markdown = 'Markdown'

class TelegramNotify:
    def __init__(self, bot_token, chat_id):
        self.token = bot_token
        self.chat_id = chat_id

    def send_msg(self, msg, parse_mode=ParseMode.TEXT, proxy=None):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"

        data = {
            'chat_id': self.chat_id,
            'text': msg,
            "parse_mode": parse_mode.value
        }

        response = requests.post(url, data=data, proxies=proxy)
        return response.text

    def send_photo(self, photo_path, caption=None, proxy=None):
        url = f"https://api.telegram.org/bot{self.token}/sendPhoto"

        data = {
            'chat_id': self.chat_id,
            "caption": caption
        }

        with open(photo_path, 'rb') as photo:
            files = {'photo': photo}
            response = requests.post(url, data=data, files=files, proxies=proxy)

        return response.text

    def send_file(self, file_path, caption=None, proxy=None):
        url = f"https://api.telegram.org/bot{self.token}/sendDocument"

        data = {
            'chat_id': self.chat_id,
            "caption": caption
        }

        with open(file_path, 'rb') as file:
            files = {'document': file}
            response = requests.post(url, data=data, files=files, proxies=proxy)

        return response.text


if __name__ == "__main__":
    TOKEN = ''
    CHAT_ID = ''
    # 可选项
    proxy = {
        "http": "http://127.0.0.1:7890",
        "https": "http://127.0.0.1:7890"
    }
    telegram = TelegramNotify(TOKEN, CHAT_ID)
    # https://core.telegram.org/bots/api#formatting-options
    # print(telegram.send_msg("[link](https://www.example.com)", ParseMode.Markdown, proxy=proxy))
    # print(telegram.send_photo("test.png","test", proxy=proxy))
    print(telegram.send_file("test.txt", "test", proxy=proxy))