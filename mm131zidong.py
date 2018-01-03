#!/usr/bin/env python
# coding=utf-8
import urllib.request
from bs4 import BeautifulSoup
import os
import shutil
import urllib.error
import pymysql
import re
def xiazai_mm131(url):
    html = urllib.request.urlopen(url)
    title = BeautifulSoup(html, 'lxml').find("title").get_text()
    title = title[:-19]
    title = title.replace(':', '')
    title = title.replace('?', '')
    title = title.replace('"', '')
    html = urllib.request.urlopen(url)
    page = BeautifulSoup(html, 'lxml').find("span", {"class": "page-ch"}).get_text()
    pattern = re.compile('\d*')
    page = pattern.findall(page)[1]
    try:
        os.makedirs("D:\\temp\\pic\\mm131\\" + title + page)
    except:
        return
    try:
        html = urllib.request.urlopen(urllib.request.Request(url))
        picurl = BeautifulSoup(html, 'lxml').find("div", {"class": "content-pic"}).find("img")["src"]
        req = urllib.request.Request(picurl)
        req.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8")
        req.add_header("Accept-Encoding","gzip,deflate")
        req.add_header("Accept-Language","zh-CN,zh;q=0.9")
        req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.25 Safari/537.36")
        req.add_header("Cookie","bdshare_firstime=1514538484412; UM_distinctid=160a187435124-03f316a3ae33c8-5d4e231d-144000-160a1874352a87; CNZZDATA3866066=cnzz_eid%3D935699110-1494676185-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1494676185; Hm_lvt_9a737a8572f89206db6e9c301695b55a=1514538490,1514565948; Hm_lpvt_9a737a8572f89206db6e9c301695b55a=1514567510")
        req.add_header("Referer","http://www.mm131.com/xinggan/3561.html")
        req.add_header("Connection","keep-alive")
        req.add_header("Host","img1.mm131.me")
        img = urllib.request.urlopen(req).read()
        f = open("D:\\temp\\pic\\mm131\\" + title + page + "\\" + "1.jpg", "wb")
        f.write(img)
        f.close()
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
            conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='mypydb', charset='utf8')
            cur = conn.cursor()
            sql = ("insert into mm131(url)" "values(%s)")
            cur.execute(sql, url)
            conn.commit()
            cur.close()
            conn.close()
            print('未下载网址已存入数据库')
        if hasattr(e, "reason"):
            print(e.reason)
            conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='mypydb', charset='utf8')
            cur = conn.cursor()
            sql = ("insert into mm131(url)" "values(%s)")
            cur.execute(sql, url)
            conn.commit()
            cur.close()
            conn.close()
            print('未下载网址已存入数据库')
    finally:
        pass
    after = int(page) + 1
    for i in range(2, after):
        try:
            url0 = url[:-5]
            url1 = url0 + '_' + str(i) + '.html'
            html = urllib.request.urlopen(urllib.request.Request(url1))
            picurl = BeautifulSoup(html, 'lxml').find("div", {"class": "content-pic"}).find("img")["src"]
            req = urllib.request.Request(picurl)
            req.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8")
            req.add_header("Accept-Encoding","gzip,deflate")
            req.add_header("Accept-Language","zh-CN,zh;q=0.9")
            req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.25 Safari/537.36")
            req.add_header("Cookie","bdshare_firstime=1514538484412; UM_distinctid=160a187435124-03f316a3ae33c8-5d4e231d-144000-160a1874352a87; CNZZDATA3866066=cnzz_eid%3D935699110-1494676185-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1494676185; Hm_lvt_9a737a8572f89206db6e9c301695b55a=1514538490,1514565948; Hm_lpvt_9a737a8572f89206db6e9c301695b55a=1514567510")
            req.add_header("Referer","http://www.mm131.com/xinggan/3561.html")
            req.add_header("Connection","keep-alive")
            req.add_header("Host","img1.mm131.me")
            img = urllib.request.urlopen(req).read()
            f = open("D:\\temp\\pic\\mm131\\" + title + page + "\\" + str(i) + ".jpg", "wb")
            f.write(img)
            f.close()
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                print(e.code)
                conn = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='mypydb',charset='utf8')
                cur = conn.cursor()                                                                             
                sql = ("insert into mm131(url)" "values(%s)")
                cur.execute(sql,url)
                conn.commit()      
                cur.close()        
                conn.close() 
                print('未下载网址已存入数据库')
            if hasattr(e,"reason"):
                print(e.reason)
                conn = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='mypydb',charset='utf8')
                cur = conn.cursor()                                                                             
                sql = ("insert into mm131(url)" "values(%s)")
                cur.execute(sql,url)
                conn.commit()      
                cur.close()        
                conn.close()
                print('未下载网址已存入数据库')
        finally:
            pass
def xiazai_mm131_sql(url):
    html = urllib.request.urlopen(url)
    title = BeautifulSoup(html,'lxml').find("title").get_text()
    title = title[:-19]
    title = title.replace(':', '')
    title = title.replace('?', '')
    title = title.replace('"', '')
    html = urllib.request.urlopen(url)
    page = BeautifulSoup(html, 'lxml').find("span", {"class": "page-ch"}).get_text()
    pattern = re.compile('\d*')
    page = pattern.findall(page)[1]
    try:
        os.makedirs("D:\\temp\\pic\\mm131\\" + title + page)
    except:
        shutil.rmtree("D:\\temp\\pic\\mm131\\" + title + page)
        os.makedirs("D:\\temp\\pic\\mm131\\" + title + page)
    try:
        html = urllib.request.urlopen(urllib.request.Request(url))
        picurl = BeautifulSoup(html,'lxml').find("div",{"class": "content-pic"}).find("img")["src"]
        req = urllib.request.Request(picurl)
        req.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8")
        req.add_header("Accept-Encoding","gzip,deflate")
        req.add_header("Accept-Language","zh-CN,zh;q=0.9")
        req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.25 Safari/537.36")
        req.add_header("Cookie","bdshare_firstime=1514538484412; UM_distinctid=160a187435124-03f316a3ae33c8-5d4e231d-144000-160a1874352a87; CNZZDATA3866066=cnzz_eid%3D935699110-1494676185-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1494676185; Hm_lvt_9a737a8572f89206db6e9c301695b55a=1514538490,1514565948; Hm_lpvt_9a737a8572f89206db6e9c301695b55a=1514567510")
        req.add_header("Referer","http://www.mm131.com/xinggan/3561.html")
        req.add_header("Connection","keep-alive")
        req.add_header("Host","img1.mm131.me")
        img = urllib.request.urlopen(req).read()
        f = open("D:\\temp\\pic\\mm131\\" + title + page + "\\" + "1.jpg", "wb")
        f.write(img)
        f.close()
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
            conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='mypydb', charset='utf8')
            cur = conn.cursor()
            sql = ("insert into mm131m(url)" "values(%s)")
            cur.execute(sql, url)
            conn.commit()
            cur.close()
            conn.close()
            print('未下载网址已存入数据库')
        if hasattr(e,"reason"):
            print(e.reason)
            conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='mypydb', charset='utf8')
            cur = conn.cursor()
            sql = ("insert into mm131m(url)" "values(%s)")
            cur.execute(sql, url)
            conn.commit()
            cur.close()
            conn.close()
            print('未下载网址已存入数据库')
    finally:
        pass
    after = int(page) + 1
    for i in range(2, after):
        try:
            url0 = url[:-5]
            url1 = url0 + '_' + str(i) + '.html'
            html = urllib.request.urlopen(urllib.request.Request(url1))
            picurl = BeautifulSoup(html,'lxml').find("div", {"class": "content-pic"}).find("img")["src"]
            req = urllib.request.Request(picurl)
            req.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8")
            req.add_header("Accept-Encoding","gzip,deflate")
            req.add_header("Accept-Language","zh-CN,zh;q=0.9")
            req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.25 Safari/537.36")
            req.add_header("Cookie","bdshare_firstime=1514538484412; UM_distinctid=160a187435124-03f316a3ae33c8-5d4e231d-144000-160a1874352a87; CNZZDATA3866066=cnzz_eid%3D935699110-1494676185-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1494676185; Hm_lvt_9a737a8572f89206db6e9c301695b55a=1514538490,1514565948; Hm_lpvt_9a737a8572f89206db6e9c301695b55a=1514567510")
            req.add_header("Referer","http://www.mm131.com/xinggan/3561.html")
            req.add_header("Connection","keep-alive")
            req.add_header("Host","img1.mm131.me")
            img = urllib.request.urlopen(req).read()
            f = open("D:\\temp\\pic\\mm131\\" + title + page + "\\" + str(i) + ".jpg", "wb")
            f.write(img)
            f.close()
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                print(e.code)
                conn = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='mypydb',charset='utf8')
                cur = conn.cursor()
                sql = ("insert into mm131m(url)" "values(%s)")
                cur.execute(sql,url)
                conn.commit()
                cur.close()
                conn.close()
                print('未下载网址已存入数据库')
            if hasattr(e,"reason"):
                print(e.reason)
                conn = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='mypydb',charset='utf8')
                cur = conn.cursor()
                sql = ("insert into mm131m(url)" "values(%s)")
                cur.execute(sql,url)
                conn.commit()
                cur.close()
                conn.close()
                print('未下载网址已存入数据库')
        finally:
            pass
if __name__ == '__main__':
    url = 'http://www.mm131.com/xinggan/'
    html = urllib.request.urlopen(url).read()
    urls = BeautifulSoup(html, 'lxml').find('dl', {'class': 'list-left public-box'}).findAll('a', {'target': '_blank'})
    print('第1页')
    for url in urls:
        url = url['href']
        print(url)
        xiazai_mm131(url)
    for i in range(4,122):
        print("第"+str(i)+"页")
        url = 'http://www.mm131.com/xinggan/list_6_'+str(i)+'.html'
        html = urllib.request.urlopen(url).read()
        urls = BeautifulSoup(html,'lxml').find('dl',{'class': 'list-left public-box'}).findAll('a',{'target': '_blank'})
        for url in urls:
            url = url['href']
            print(url)
            xiazai_mm131(url)
    urls = []
    conn = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='mypydb',charset='utf8')
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
            conn = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='mypydb',charset='utf8')
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

