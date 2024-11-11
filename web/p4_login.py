import requests

def login_to_website(url, username, password):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    login_data = {
        'username': username,
        'password': password
    }
    
    response = requests.post(url, data=login_data, headers=headers)
    
    if response.status_code == 200:
        print("登录成功")
        # 假设token在响应的cookies中
        token = response.cookies.get('token')
        return token
    else:
        print("登录失败，状态码：", response.status_code)
        return None

def query_data_with_token(url, token):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Authorization': f'Bearer {token}'  # 假设使用Bearer token进行认证
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("查询成功")
        return response.json()  # 假设返回的是JSON数据
    else:
        print("查询失败，状态码：", response.status_code)
        return None

# 示例使用
login_url = 'https://example.com/login'
query_url = 'https://example.com/data'  # 替换为实际的数据查询URL
username = 'your_username'
password = 'your_password'

token = login_to_website(login_url, username, password)
if token:
    data = query_data_with_token(query_url, token)
    if data:
        print(data)



