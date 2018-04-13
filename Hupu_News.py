from Get_soup import get_soup
from urls_quchong import urls_quchong
from get_urls import get_all_urls
import re
import datetime
import time

soup=get_soup("https://nba.hupu.com")
re_text="^(https://nba.hupu.com)"
urls=get_all_urls(soup,re_text)
#print(urls)
urls_new=urls_quchong(urls)
#print(urls_new)
all_links=[]
for url in urls_new:
    soup=get_soup(url)
    #print(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")+'\n====================================')
    time.sleep(1)
    re_text1="^(https://)"
    urls=get_all_urls(soup,re_text1)
    all_links.append(urls)
print(all_links)
all_urls=urls_quchong(all_links)
print(all_urls)
print(len(all_urls))