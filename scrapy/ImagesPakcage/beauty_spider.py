#!/usr/bin/python
import requests
import re,sys,random

"""
https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%C3%C0%C5%AE%CD%BC%C6%AC&fr=ala&ala=1&alatpl=cover&pos=0&hs=2&xthttps=111111
爬取 以上URL的所有图片 
regex="data-imgurl="https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1193487199,2202550203&fm=23&gp=0.jpg"/>"
"""
get = requests.get
url="https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%C3%C0%C5%AE%CD%BC%C6%AC&fr=ala&ala=1&alatpl=cover&pos=0&hs=2&xthttps=111111"
"""u1='data:image/jpeg;base64,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'
rs1=get(u1)
try:
    rs1=get("https://data:image/jpeg;base64,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")
    rs2=get("https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1193487199,2202550203&fm=23&gp=0.jpg")
    print(rs1)
    print(rs2)
except:
    print("could not scrapy!")
    sys.exit(0)"""
"""
regex = 
 "thumbURL":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1288986746,2781587069&fm=23&gp=0.jpg"
"""


def get_img_url(url):
    try:
        res= get(url)
    except:
        print("Could not open this url")
        sys.exit(0)
    res.encoding="utf-8"
    html  =res.text
    regex =r'"thumbURL":"https://(.+?\.jpg)"'
    #regex= r'data:image'
    #regex=r'data-imgurl="(https://\.+?\.jpg)"'
    pat = re.compile(regex)
    urls =(re.findall(pat,html))
    for i in range(0,urls.__len__()):
        urls[i] = "https://" + urls[i]
    return urls


def img_downloads(imgurl):
    length = imgurl.__len__()
    file_name = imgurl[length-15:length]
    res  = get(imgurl)
    with open("./Images/hello"+file_name,"wb") as f1:
       for chunk in res.iter_content(chunk_size=1024):
           if chunk:
               f1.write(chunk)
               f1.flush()
    f1.close()


urls=get_img_url(url)
for i in urls:
    print(i,)
    img_downloads(i)
