import re
def get_all_urls(soup,re_text):
    '''输入正则表达式的过滤规则'''
    links=soup.findAll("a", href=re.compile(re_text))
    urls=[]
    for link in links:
        url=link['href']
        urls.append(url)
    return urls


