import requests

class ResendNotify:
    def __init__(self, api_key):
        self.api_key = api_key

    def send_email(self, from_addr, to_addr, subject, html_content):
        url = "https://api.resend.com/emails"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "from": from_addr,
            "to": [to_addr],
            "subject": subject,
            "html": html_content,
        }

        response = requests.post(url, headers=headers, json=data)

        return response.json()


if __name__ == "__main__":
    API_KEY = ""
    resend = ResendNotify(API_KEY)
    print(resend.send_email("", "", "Test Subject", "<h1>This is a test email</h1>"))