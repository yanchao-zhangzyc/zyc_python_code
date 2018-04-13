def urls_quchong(urls):
    urls_new=[]
    for url in urls:
        if urls not in urls_new:
            urls_new.append(url)
    return urls_new
