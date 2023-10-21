import requests
import re

# 访问网址
r = requests.get("https://www.bilibili.com/")

# 编码格式
def r_encoding():
    # 从HTTP header中猜测的响应内容编码方式
    print(r.encoding)
    # 从内容中分析出的响应内容编码方式（备选编码方式）
    print(r.apparent_encoding)
    # 更改编码格式为utf-8
    r.encoding = 'utf-8'

# 性质
def r_property():
    # 打印状态码(200表示连接成功，404表示失败（虽然说只要不是200就都是失败的就对了）)
    print(r.status_code)
    # 检测类型
    print(type(r))

# 内容信息
def r_content():
    # HTTP响应的二进制形式
    print(r.content)
    # 获得页面头部信息
    print(r.headers)
    # 打印网页内容（HTTP响应的字符串形式）
    print(r.text)
