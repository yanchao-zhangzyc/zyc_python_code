# encoding=utf-8
import requests
import datetime
from bs4 import BeautifulSoup
import time
import re

'''获取网页上新闻链接地址'''
url = "https://voice.hupu.com/nba"
html = requests.get(url)
soup = BeautifulSoup(html.text)
links_text = soup.findAll("a", href=re.compile("^(https://voice.hupu.com/nba/)"))

urls = []

for link in links_text:
    # 获取url链接，并将链接存入数组中
    url = link['href']
    urls.append(url)
    print(url)


# 链接去重复
def remove_duplicates(urls):
    urls_new = []
    for url in urls:
        if url not in urls_new:
            urls_new.append(url)
    return urls_new


urls_new = remove_duplicates(urls)
# 获取新闻文本并存入到txt文件中
fb = open('Hupu_NBA-news' + datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + '.txt',
          'w', encoding='utf-8')

for url in urls_new:
    try:
        html = requests.get(url)
        bs0bj = BeautifulSoup(html.text, "html.parser")
        # 获取新闻文本
        news_content = bs0bj.find(class_="artical-main-content").get_text()
        # 文件文本写入
        fb.write(news_content)
        print(news_content, '\n===============================================')
        print(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))
        time.sleep(1)
    except Exception as e:
        print(e)
        continue