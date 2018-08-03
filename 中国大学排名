import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:#寻找的是在tbody下面的所有tr，一个tr就是一个学校整个的信息,for的作用就是一个tr一循环，这就是问什么 ulist只有三个变量，而且是三个一循环，在不同大学里循环
        print(tr)
        if isinstance(tr,bs4.element.Tag):#筛出tr中的非标签元素
            tds = tr.find_all('td')  # tr.find_all() 的缩写 是一个list格式，意思是tr下的所有td标签，一个td就是一个信息单元，比如清华的信息单元是 排名 分数
            print("-----------tds----------")
            print(tds)
            print("-----------tds----------")
            ulist.append([tds[0].string,tds[1].string,tds[2].string])

def printUnivList(ulist,num):
    print('{:^10}\t{:^20}\t{:^20}'.format('排名','学校','省份'))
    for i in range(num):
        u = ulist[i]
        print('{:^10}\t{:^20}\t{:^20}'.format(u[0],u[1],u[2]))

def start():
    uinfo = []
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html"
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)

start()

