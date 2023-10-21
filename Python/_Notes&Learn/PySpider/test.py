import requests

r = requests.get("https://www.bilibili.com/")

print(r.content)
