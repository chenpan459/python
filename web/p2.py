import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 搜索关键字
keyword = '凡人修仙传'

# 搜索URL（假设网站支持通过URL参数进行搜索）
search_url = f'https://search.bilibili.com/all?keyword={keyword}'
#https://search.bilibili.com/all?keyword=%E5%87%A1%E4%BA%BA%E4%BF%AE%E4%BB%99%E4%BC%A0&from_source=webtop_search&spm_id_from=333.1007&search_source=2

# 发送HTTP请求
# response = requests.get(search_url)
response = requests.get(search_url, headers=headers)


# # 检查请求是否成功
# if response.status_code == 200:
#     # 解析网页内容
#     soup = BeautifulSoup(response.content, 'html.parser')
#     print(soup)
    
#     # 查找视频URL（假设视频URL在video标签的src属性中）
#     video_tags = soup.find_all('video')
#     if video_tags:
#         for i, video_tag in enumerate(video_tags):
#             if 'src' in video_tag.attrs:
#                 video_url = video_tag['src']
                
#                 # 下载视频
#                 video_response = requests.get(video_url, stream=True)
#                 if video_response.status_code == 200:
#                     with open(f'video_{i}.mp4', 'wb') as file:
#                         for chunk in video_response.iter_content(chunk_size=1024):
#                             if chunk:
#                                 file.write(chunk)
#                     print(f'视频 {i} 下载完成')
#                 else:
#                     print(f'视频 {i} 下载失败，状态码: {video_response.status_code}')
#     else:
#         print('未找到视频标签')
# else:
#     print(f'请求失败，状态码: {response.status_code}')
