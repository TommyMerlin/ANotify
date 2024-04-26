import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailNotify:
    def __init__(self, mail_host, mail_user, mail_pass, sender):
        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_pass = mail_pass
        self.sender = sender
        # 设置email信息
        self.message = MIMEMultipart()
        # 发送方信息
        self.message['From'] = sender

    # 添加附件
    def add_attachment(self, attachment_filename):
        attachment = MIMEText(open(attachment_filename,'rb').read(), 'base64', 'utf-8')
        attachment.add_header("Content-Type","application/octet-stream")
        attachment.add_header("Content-Disposition", "attachment", filename=attachment_filename)
        self.message.attach(attachment)

    def send_email(self, subject, text, attachment_filename = None, receiver = '786731256@qq.com'):
        """发送邮件
        :subject:               主题
        :text:                  正文
        :attachment_filename:   附件文件名
        :receiver:              收信地址
        :return:                发送是否成功
        """

        # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
        receivers = [receiver]

        # 正文内容
        msg = MIMEText(text,'plain','utf-8')

        self.message.attach(msg)
        # 邮件主题
        self.message['Subject'] = subject

        # 接受方信息
        self.message['To'] = receivers[0]

        if attachment_filename is not None:
            self.add_attachment(attachment_filename)

        # 登录并发送邮件
        try:
            smtpObj = smtplib.SMTP()
            # 连接到服务器
            smtpObj.connect(self.mail_host,25)
            # 登录到服务器
            smtpObj.login(self.mail_user, self.mail_pass)
            # 发送
            smtpObj.sendmail(self.sender,receivers,self.message.as_string())
            # 退出
            smtpObj.quit()
            return True
        except smtplib.SMTPException as e:
            return False

if __name__ == "__main__":
    # 邮箱服务器地址
    MAIL_HOST = ''
    # 用户名
    MAIL_USER = ''
    # 密码(部分邮箱为授权码)
    MAIL_PASS = ''
    # 邮件发送方邮箱地址
    SENDER = ''

    email_notify = EmailNotify(MAIL_HOST, MAIL_USER, MAIL_PASS, SENDER)
    if email_notify.send_email("测试标题", "测试正文", attachment_filename=None, receiver='123@example.com'):
        print("邮件发送成功√")
    else:
        print("邮件发送失败×")