## 安装
```console
pip install anotify
```
## 实例
- 企业微信
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
wn.send_msg("./test.png")
```
- AnPush
```python
from ANotify import Nanpush
TOKEN = ""
anpush = ANotify.AnpushNotify(TOKEN)
anpush.send_msg("title", "content", "channel_id")
```
- IYUU
```python
from ANotify import Niyuu
TOKEN = ""
iyuu = Niyuu.IyuuNotify(TOKEN)
iyuu.send_msg("title", "content")
```
- PushPlus
```python
from ANotify import NPushPlus
TOKEN = ''
pushplus = NPushPlus.PushPlusNotify(TOKEN)
pushplus.send_msg("测试标题", "测试正文", TemplateType.txt)
```
- Server酱
```python
from ANotify import Nserverchan
TOKEN = ''
serverchan = Nserverchan.ServerChanNotify(TOKEN)
serverchan.send_msg("测试标题", "测试正文")
```
- Email
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
