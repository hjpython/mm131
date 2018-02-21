#!/usr/bin/env python
# coding=utf-8
import urllib.request
from bs4 import BeautifulSoup
import os
import shutil
import urllib.error
import re
from factor import *
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
        req(picurl)
        img = urllib.request.urlopen(req).read()
        f = open("D:\\temp\\pic\\mm131\\" + title + page + "\\" + "1.jpg", "wb")
        f.write(img)
        f.close()
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
            sql(url)
            print('未下载网址已存入数据库')
        if hasattr(e, "reason"):
            print(e.reason)
            sql(url)
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
            req(picurl)
            img = urllib.request.urlopen(req).read()
            f = open("D:\\temp\\pic\\mm131\\" + title + page + "\\" + str(i) + ".jpg", "wb")
            f.write(img)
            f.close()
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                print(e.code)
                sql(url)
                print('未下载网址已存入数据库')
            if hasattr(e,"reason"):
                print(e.reason)
                sql(url)
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
        req(picurl)
        img = urllib.request.urlopen(req).read()
        f = open("D:\\temp\\pic\\mm131\\" + title + page + "\\" + "1.jpg", "wb")
        f.write(img)
        f.close()
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
            sql(url)
            print('未下载网址已存入数据库')
        if hasattr(e,"reason"):
            print(e.reason)
            sql(url)
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
            req(picurl)
            img = urllib.request.urlopen(req).read()
            f = open("D:\\temp\\pic\\mm131\\" + title + page + "\\" + str(i) + ".jpg", "wb")
            f.write(img)
            f.close()
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                print(e.code)
                sql(url)
                print('未下载网址已存入数据库')
            if hasattr(e,"reason"):
                print(e.reason)
                sql(url)
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
    for i in range(2,130):
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