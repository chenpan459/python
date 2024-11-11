import requests
from bs4 import BeautifulSoup

# 目标网址
url = 'https://arthurchiao.art/'

# 发送HTTP请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 获取网页内容
    html_content = response.text
    
    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 示例：获取网页中的所有段落文本
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        #paragraph = paragraph.encode('utf-8', errors='ignore').decode('utf-8')
        #print(paragraph)
        #paragraph = paragraph.encode('utf-8', errors='ignore').decode('utf-8')
        print(paragraph)
        # 或者替换错误字符
        #paragraph = paragraph.encode('gbk', errors='replace').decode('gbk')
        #print(paragraph)


else:
    print(f"请求失败，状态码：{response.status_code}")
