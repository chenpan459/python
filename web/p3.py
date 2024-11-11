import requests
from bs4 import BeautifulSoup

# 搜索关键字
keyword = 'your_keyword'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 搜索URL（假设网站支持通过URL参数进行搜索）
search_url = f'https://www.example.com/search?q={keyword}'

# 发送HTTP请求
#response = requests.get(search_url)
response = requests.get(search_url, headers=headers)


# 检查请求是否成功
if response.status_code == 200:
    # 解析网页内容
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 查找MP3文件URL（假设MP3文件URL在audio标签的src属性中）
    audio_tags = soup.find_all('audio')
    if audio_tags:
        for i, audio_tag in enumerate(audio_tags):
            if 'src' in audio_tag.attrs:
                mp3_url = audio_tag['src']
                
                # 下载MP3文件
                mp3_response = requests.get(mp3_url, stream=True)
                if mp3_response.status_code == 200:
                    with open(f'song_{i}.mp3', 'wb') as file:
                        for chunk in mp3_response.iter_content(chunk_size=1024):
                            if chunk:
                                file.write(chunk)
                    print(f'MP3文件 {i} 下载完成')
                else:
                    print(f'MP3文件 {i} 下载失败，状态码: {mp3_response.status_code}')
    else:
        print('未找到音频标签')
else:
    print(f'请求失败，状态码: {response.status_code}')
