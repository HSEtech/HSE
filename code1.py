import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url,headers=kv,timeout=30)
        print(r.status_code)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "无内容 "


def parserHTML(html):
    soup = BeautifulSoup(html, 'html.parser')
    content = []
    for mulu in soup.find_all(class_='mulu'):
        #print(mulu)
        h2 = mulu.find('h2')
        if h2 !=None:
            h2_title = h2.text
            list=[]
            for a in mulu.find(class_='box').find_all('a'):
                print(a)
                herf = a.get('href')
                box_title = a.get('title')
                list.append({'box_title':box_title,'href':herf})
            content.append({'title':h2_title,'content':list})
            #print(content)





def main():
    url = 'http://seputu.com'
    html = getHTMLText(url)
    parserHTML(html)

main()