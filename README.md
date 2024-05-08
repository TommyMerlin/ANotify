![Alt](https://repobeats.axiom.co/api/embed/e1ca45165d69b8370c78d60260a6474b49621fac.svg "Repobeats analytics image")

## 安装
```console
pip install anotify
```

## 实例
### 企业微信
[官网](https://work.weixin.qq.com/)
```python
from ANotify import Nwecom
# 企业ID
CORPID = ''
# 应用Secret
CORPSECRET = ''
# 应用ID
AgentId = ''

wn = Nwecom.WxNotify(corpid=CORPID, corpsecret=CORPSECRET, agentid=AgentId)
wn.send_msg("test message")
wn.send_text_card("test title", "test content", "https://www.example.com")
wn.send_file("./test.txt")
wn.send_img("./test.png")
```

### AnPush
[官网](https://anpush.com/)
```python
from ANotify import Nanpush
TOKEN = ""
anpush = Nanpush.AnpushNotify(TOKEN)
anpush.send_msg("title", "content", "channel_id")
```

### IYUU
[官网](https://iyuu.cn/)
```python
from ANotify import Niyuu
TOKEN = ""
iyuu = Niyuu.IyuuNotify(TOKEN)
iyuu.send_msg("title", "content")
```

### PushPlus
[官网](https://www.pushplus.plus/)
```python
from ANotify import NPushPlus
TOKEN = ''
pushplus = Npushplus.PushPlusNotify(TOKEN)
pushplus = Npushplus.PushPlusNotify(TOKEN)
pushplus.send_msg("测试标题", "测试正文", Npushplus.TemplateType.txt)
msg_json = {
    "status": 200,
    "msg": "success"
}
pushplus.send_msg("测试标题", msg_json, Npushplus.TemplateType.json)
pushplus.send_msg("测试标题", "**测试内容**\n- test1\n- [ANotify](https://github.com/TommyMerlin/ANotify)", Npushplus.TemplateType.markdown)
pushplus.send_msg("测试标题", "测试内容<a href='https://github.com/TommyMerlin/ANotify'>ANotify</a>", Npushplus.TemplateType.html)
```

### Server酱
[官网](https://sct.ftqq.com/)
```python
from ANotify import Nserverchan
TOKEN = ''
serverchan = Nserverchan.ServerChanNotify(TOKEN)
serverchan.send_msg("测试标题", "测试正文")
```

### Telegram Bot
[官网](https://core.telegram.org/bots)
```python
from ANotify import Ntelegram
TOKEN = ''
CHAT_ID = ''
# 可选项
proxy = {
        "http": "http://127.0.0.1:1234",
        "https": "http://127.0.0.1:1234"
}
telegram = Ntelegram.TelegramNotify(TOKEN, CHAT_ID)

# https://core.telegram.org/bots/api#formatting-options
telegram.send_msg("test message", Ntelegram.ParseMode.TEXT)   # 无代理
telegram.send_msg("test message", Ntelegram.ParseMode.TEXT, proxy=proxy) # 有代理
telegram.send_msg("[link](https://www.example.com)", Ntelegram.ParseMode.Markdown)
telegram.send_msg("<a href='https://www.example.com'>link</a>", Ntelegram.ParseMode.HTML)
telegram.send_photo("test.png","test")
telegram.send_file("test.txt", "test")
```

### Email
```python
from ANotify import Nemail
# 邮箱服务器地址
MAIL_HOST = ''
# 用户名
MAIL_USER = ''
# 密码(部分邮箱为授权码)
MAIL_PASS = ''
# 邮件发送方邮箱地址
SENDER = ''

email_notify = Nemail.EmailNotify(MAIL_HOST, MAIL_USER, MAIL_PASS, SENDER)
if email_notify.send_email("测试标题", "测试正文", attachment_filename=None, receiver='123@example.com'):
    print("邮件发送成功√")
else:
    print("邮件发送失败×")
```
