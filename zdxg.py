#!/usr/bin/env python
# coding=utf-8
from factor import *
from multiprocessing import Pool

if __name__ == '__main__':
    #下载第1页的图片
    p = Pool(50)
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
        p.apply_async(xiazai_mm131, args=(url,))

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
            p.apply_async(xiazai_mm131, args=(url,))

    #下载数据库中图片
    urls = []
    conn = pymysql.connect(**kw)
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
        p.apply_async(xiazai_mm131_sql, args=(url,))
        try:
            conn = pymysql.connect(**kw)
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
    p.close()
    p.join()
    print('\n')
    print('恭喜您，已全部下载完毕')