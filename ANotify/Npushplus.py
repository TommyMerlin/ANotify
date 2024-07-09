import requests
from enum import Enum
import json
import httpx
import asyncio

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

    async def send_msg_async(self, msg_title, msg_text, template_type=TemplateType.txt):
        """异步发送消息
        :msg_title: 主题
        :msg_text:  正文
        :return:    发送结果
        """
        data = {
            "token": self.token,
            "title": msg_title,
            "content": msg_text,
            "template": template_type.value,
            "channel": "wechat"
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(self.base_url, data=json.dumps(data))
            response.raise_for_status()
            return response.json()

    def send_msg(self, msg_title, msg_text, template_type=TemplateType.txt):
        """同步发送消息
        :msg_title: 主题
        :msg_text:  正文
        :return:    发送结果
        """
        # 这里使用同步客户端，调用异步方法
        return asyncio.run(self.send_msg_async(msg_title, msg_text, template_type))

if __name__ == "__main__":
    TOKEN = ''
    notify = PushPlusNotify(TOKEN)

    print(notify.send_msg("测试标题", "测试正文", TemplateType.txt))
    async def main():
        result = await notify.send_msg_async("测试标题异步", "测试正文异步", TemplateType.txt)
        print(result)
    
    asyncio.run(main())

