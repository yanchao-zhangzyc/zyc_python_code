import datetime
import requests
from bs4 import BeautifulSoup
import time
import re
from Get_soup import get_soup
soup=get_soup("http://photo.hupu.com/nba")
pic_links=soup.findAll(src=re.compile("^(//)"))
for link in pic_links:
    url=link['src']
    try:
        html=requests.get("http:"+url)
        with open(str(datetime.datetime.now())+".jpg",'wb') as fb:
            fb.write(html.content)
            fb.close()
    except Exception as e:
        print(e)




