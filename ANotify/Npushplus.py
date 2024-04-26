import requests
from enum import Enum
import json

class TemplateType(Enum):
    html = 'html'                   # 默认模板，支持html文本
    txt = 'txt'                     # 纯文本展示，不转义html
    json = 'json'                   # 内容基于json格式展示
    markdown = 'markdown'           # 内容基于markdown格式展示
    cloudMonitor = 'cloudMonitor'   # 阿里云监控报警定制模板
    jenkins = 'jenkins'             # jenkins插件定制模板
    route = 'route'                 # 路由器插件定制模板
    pay = 'pay'                     # 支付成功通知模板

class PushPlusNotify:
    def __init__(self, token):
        self.token = token
        self.base_url = 'http://www.pushplus.plus/send'

    # https://www.pushplus.plus/doc/guide/api.html#%E4%B8%80%E3%80%81%E5%8F%91%E9%80%81%E6%B6%88%E6%81%AF%E6%8E%A5%E5%8F%A3
    def send_msg(self, msg_title, msg_text, template_type=TemplateType.html):
        """发送消息
        :msg_title: 主题
        :msg_text:  正文
        :return:    发送是否成功
        """

        data = {
            "token": self.token,
            "title": msg_title,
            "content": msg_text,
            "template": template_type.value,
            "channel": "wechat"
        }

        response = requests.post(self.base_url, data=json.dumps(data))
        response.raise_for_status()
        return response.json()

if __name__ == "__main__":
    TOKEN = ''
    print(PushPlusNotify(TOKEN).send_msg("测试标题", "测试正文", TemplateType.txt))

