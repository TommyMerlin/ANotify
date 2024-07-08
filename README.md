![Alt](https://repobeats.axiom.co/api/embed/e1ca45165d69b8370c78d60260a6474b49621fac.svg "Repobeats analytics image")
[![Upload Python Package](https://github.com/TommyMerlin/ANotify/actions/workflows/python-publish.yml/badge.svg)](https://github.com/TommyMerlin/ANotify/actions/workflows/python-publish.yml)

## 安装
```console
pip install anotify
```

## 实例
### 企业微信
[官网](https://work.weixin.qq.com/)  
[群聊机器人Webhook](https://open.work.weixin.qq.com/help2/pc/14931)
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
wn.send_msg_markdown("**Hello**\n- test1\n- [ANotify](https://github.com/TommyMerlin/ANotify)")
wn.send_text_card("test title", "test content", "https://www.example.com")
wn.send_file("./test.txt")
wn.send_img("./test.png")

# Webhook
WEB_HOOK = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxx"
wn_webhook = Nwecom.WxWebhookNotify(WEB_HOOK)
wn_webhook.send_msg("Hello")
wn_webhook.send_msg_markdown("**Hello**\n- test1\n- [ANotify](https://github.com/TommyMerlin/ANotify)")
wn_webhook.send_img("E:/Desktop/gpt/Cursor_Demo/test.png")
wn_webhook.send_file("test.png")
```

### 飞书
[官网](https://open.feishu.cn/document/server-docs/im-v1/introduction)  
[创建应用](https://open.feishu.cn/document/home/introduction-to-custom-app-development/self-built-application-development-process)  
[API调试台](https://open.feishu.cn/api-explorer?from=op_doc_tab)  
[获取消息发送对象 openid](https://open.feishu.cn/document/faq/trouble-shooting/how-to-obtain-openid)  
[Webhook请求发送消息](https://open.feishu.cn/document/client-docs/bot-v3/add-custom-bot#355ec8c0)
```python
from ANotify import Nfeishu
APPID = ''
APPSECRET = ''
OPEN_ID = ''
UNION_ID = ''
USER_ID = ''
CHAT_ID = ''

feishu = Nfeishu.FeishuNotify(appid=APPID, appsecret=APPSECRET)
feishu.send_msg(Nfeishu.ReceiverType.OPEN_ID, OPEN_ID, "Hello World!")
feishu.send_msg(Nfeishu.ReceiverType.UINION_ID, UNION_ID, "Hello World!")
feishu.send_msg(Nfeishu.ReceiverType.USER_ID, USER_ID, "Hello World!")
feishu.send_msg(Nfeishu.ReceiverType.CHAT_ID, CHAT_ID, "Hello World!")
# 发送图片
feishu.send_img(Nfeishu.ReceiverType.OPEN_ID, OPEN_ID, "test.png")
# 发送文件
feishu.send_file(Nfeishu.ReceiverType.OPEN_ID, OPEN_ID, "test.txt")

# Webhook
feishu_webhook = Nfeishu.FeishuWebhookNotify("https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxx")
feishu_webhook.send_msg("Hello World!")
```

### 钉钉 
[Webhook请求发送消息](https://open.dingtalk.com/document/robots/custom-robot-access)
```python
from ANotify import Ndingtalk

WEB_HOOK = "https://oapi.dingtalk.com/robot/send?access_token=xxxxxx"
dingtalk_webhook = Ndingtalk.DingtalkWebhookNotify(WEB_HOOK)
dingtalk_webhook.send_msg("Hello World!")
```

### Gotify
[官网](https://gotify.net/docs/)
```python
from ANotify import Ngotify
TOKEN = ""
SERVER_URL = ""
gotify = Ngotify.GotifyNotify(SERVER_URL, TOKEN)
gotify.send_msg("title", "content")
gotify.send_msg("title", "**content**\n- No.1\n- No.2", Ngotify.MessageType.markdown)
```

### Ntfy
[官网](https://docs.ntfy.sh/publish/)
```python
from ANotify import Nntfy
TOPIC = ""
URL = ""
ntfy = Nntfy.NtfyNotify(TOPIC, URL)
ntfy.send_msg("title", "content")
```

### AnPush
[官网](https://anpush.com/)
```python
from ANotify import Nanpush
TOKEN = ""
anpush = Nanpush.AnpushNotify(TOKEN)
anpush.send_msg("title", "content", "channel_id")
```

### 息知
[官网](https://xz.qqoq.net/)
```python
from ANotify import Nxizhi
TOKEN = ""
xizhi = Nxizhi.XizhiNotify(TOKEN)
xizhi.send_msg("title", "content")
```

### 传息
[官网](https://cx.super4.cn/)
```python
from ANotify import Nchuanxi
TOKEN = ""
chuanxi = Nchuanxi.ChuanxiNotify(TOKEN)
chuanxi.send_msg("title", "content")
```

### WPush
[官网](https://wpush.cn)
```python
from ANotify import Nwpush
TOKEN = ""
wpush = Nwpush.WpushNotify(TOKEN)
wpush.send_msg("title", "content")
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
email_notify.send_email("测试标题", "测试正文", attachment_filename=None, receiver='123@example.com')
```