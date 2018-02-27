#!/usr/bin/env python
# coding=utf-8
from factor import *

if __name__ == '__main__':
    #下载第1页的图片
    url = 'http://www.mm131.com/xinggan/'
    html = urllib.request.urlopen(url).read()
    try:
        htmll = gzip.decompress(html).decode('gb2312','ignore')
        urls = BeautifulSoup(htmll,'lxml').find('dl',{'class':'list-left public-box'}).findAll('a',{'target':'_blank'})
    except:
        html = html.decode('gb2312','ignore')
        urls = BeautifulSoup(html,'lxml').find('dl',{'class':'list-left public-box'}).findAll('a',{'target':'_blank'})
    print('第1页')
    for url in urls:
        url = url['href']
        print(url)
        xiazai_mm131(url)
    #下载第2页到129页的图片
    for i in range(2,130):
        print("第"+str(i)+"页")
        url = 'http://www.mm131.com/xinggan/list_6_'+str(i)+'.html'
        html = urllib.request.urlopen(url).read()
        try:
            htmll = gzip.decompress(html).decode('gb2312','ignore')
            urls = BeautifulSoup(htmll,'lxml').find('dl', {'class':'list-left public-box'}).findAll('a',{'target': '_blank'})
        except:
            html = html.decode('gb2312','ignore')
            urls = BeautifulSoup(html,'lxml').find('dl', {'class':'list-left public-box'}).findAll('a',{'target': '_blank'})
        for url in urls:
            url = url['href']
            print(url)
            xiazai_mm131(url)
    #下载数据库中图片
    urls = []
    conn = pymysql.connect(host='192.168.1.6',user='root',passwd='123456',db='mypydb',charset='utf8')
    cur = conn.cursor()
    cur.execute("select url from mm131")
    results = cur.fetchall()
    cur.close()
    conn.close()
    result = list(results)
    for r in result:
        urls.append("%s"%r)
    urls = list(set(urls))
    while urls:
        url = urls.pop()
        print("重新下载:%s"%url)
        xiazai_mm131_sql(url)
        try:
            conn = pymysql.connect(host='192.168.1.6',user='root',passwd='123456',db='mypydb',charset='utf8')
            cur = conn.cursor()
            cur.execute("select url from mm131m")
            results = cur.fetchall()
            cur.execute("truncate mm131m")
            cur.close()    
            conn.close()
            result = list(results)
            for r in result:
                urls.append("%s"%r)
            urls = list(set(urls))
        except:
            pass
