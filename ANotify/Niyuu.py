import requests

class IyuuNotify:
    """用于发送通知消息到IYUU平台的客户端"""
    
    BASE_URL = "https://iyuu.cn/"
    
    def __init__(self, token):
        """
        初始化IYUU通知客户端
        
        Args:
            token: IYUU平台的访问令牌
        """
        self.token = token
    
    def send_msg(self, title, content):
        """
        发送通知消息
        
        Args:
            title: 消息标题
            content: 消息内容
            
        Returns:
            返回API响应文本
            
        Raises:
            requests.RequestException: 当请求失败时抛出
        """
        try:
            url = f"{self.BASE_URL}{self.token}.send"
            params = {"text": title, "desp": content}
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"发送消息失败: {e}")
            raise


if __name__ == "__main__":
    TOKEN = ""  # 请在这里填入你的IYUU令牌
    iyuu = IyuuNotify(TOKEN)
    print(iyuu.send_msg("测试标题", "测试内容"))
