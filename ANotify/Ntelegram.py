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
        # url = f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.chat_id}&text={msg}&parse_mode={parse_mode.value}"
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"

        querystring = {
            "chat_id": self.chat_id,
            "text": msg,
            "parse_mode": parse_mode.value
        }

        response = requests.get(url, params=querystring, proxies=proxy)
        return response.text


if __name__ == "__main__":
    TOKEN = ""
    CHAT_ID = ""
    # 可选项
    proxy = {
        "http": "http://127.0.0.1:1234",
        "https": "http://127.0.0.1:1234"
    }
    telegram = TelegramNotify(TOKEN, CHAT_ID)
    # https://core.telegram.org/bots/api#formatting-options
    print(telegram.send_msg("[link](https://www.example.com)", ParseMode.Markdown, proxy=proxy))