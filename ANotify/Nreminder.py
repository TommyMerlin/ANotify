from ._http import http_transport

class ReminderNotify:
    def __init__(self, pushkey):
        self.pushkey = pushkey

    def send_msg(self, title, desp):
        url = f"https://reminderapi.joyslinktech.com/v1/push/key/{self.pushkey}"

        querystring = {
            "title": title,
            "description": desp,
            "pushType": "1"
            }

        response = http_transport.get(url, params=querystring)

        print(response.json())


if __name__ == "__main__":
    PUSH_KEY = ""
    reminder = ReminderNotify(PUSH_KEY)
    print(reminder.send_msg("title", "content"))
