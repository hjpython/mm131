import urllib.request
import pymysql
import os
import shutil
import urllib.error
import re
from bs4 import BeautifulSoup
import gzip
from config import dir,kw

def req_add(picurl):
    req = urllib.request.Request(picurl)
    req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8")
    req.add_header("Accept-Encoding", "gzip,deflate")
    req.add_header("Accept-Language", "zh-CN,zh;q=0.9")
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.25 Safari/537.36")
    req.add_header("Cookie",
                   "bdshare_firstime=1514538484412; UM_distinctid=160a187435124-03f316a3ae33c8-5d4e231d-144000-160a1874352a87; CNZZDATA3866066=cnzz_eid%3D935699110-1494676185-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1494676185; Hm_lvt_9a737a8572f89206db6e9c301695b55a=1514538490,1514565948; Hm_lpvt_9a737a8572f89206db6e9c301695b55a=1514567510")
    req.add_header("Referer", "http://www.mm131.com/xinggan/3561.html")
    req.add_header("Connection", "keep-alive")
    req.add_header("Host", "img1.mm131.me")
    return req

def sql(url):
    conn = pymysql.connect(**kw)
    cur = conn.cursor()
    sql = ("insert into mm131(url)" "values(%s)")
    cur.execute(sql, url)
    conn.commit()
    cur.close()
    conn.close()

def xiazai_mm131(url):
    try:
        html = urllib.request.urlopen(url).read()
        try:
            htmll = gzip.decompress(html).decode('gb2312','ignore')
            title = BeautifulSoup(htmll,'lxml').find("title").get_text()
        except:
            html = html.decode('gb2312','ignore')
            title = BeautifulSoup(html,'lxml').find("title").get_text()
        title = title[:-19]
        title = title.replace(':', '')
        title = title.replace('?', '')
        title = title.replace('"', '')
        html = urllib.request.urlopen(url).read()
        try:
            htmll = gzip.decompress(html).decode('gb2312','ignore')
            page = BeautifulSoup(htmll,'lxml').find("span", {"class":"page-ch"}).get_text()
        except:
            html = html.decode('gb2312','ignore')
            page = BeautifulSoup(html,'lxml').find("span", {"class":"page-ch"}).get_text()
        pattern = re.compile('\d*')
        page = pattern.findall(page)[1]
        os.makedirs(dir + title + page)
    except:
        return
    try:
        html = urllib.request.urlopen(url).read()
        try:
            htmll = gzip.decompress(html).decode('gb2312','ignore')
            picurl = BeautifulSoup(htmll,'lxml').find("div", {"class": "content-pic"}).find("img")["src"]
        except:
            html = html.decode('gb2312','ignore')
            picurl = BeautifulSoup(html,'lxml').find("div", {"class": "content-pic"}).find("img")["src"]
        req = req_add(picurl)
        img = urllib.request.urlopen(req).read()
        f = open(dir + title + page + "\\" + "1.jpg", "wb")
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
            html = urllib.request.urlopen(url1).read()
            try:
                htmll = gzip.decompress(html).decode('gb2312','ignore')
                picurl = BeautifulSoup(htmll,'lxml').find("div", {"class": "content-pic"}).find("img")["src"]
            except:
                html = html.decode('gb2312','ignore')
                picurl = BeautifulSoup(html,'lxml').find("div", {"class": "content-pic"}).find("img")["src"]
            req = req_add(picurl)
            img = urllib.request.urlopen(req).read()
            f = open(dir + title + page + "\\" + str(i) + ".jpg", "wb")
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
    try:
        html = urllib.request.urlopen(url).read()
        try:
            htmll = gzip.decompress(html).decode('gb2312','ignore')
            title = BeautifulSoup(htmll,'lxml').find("title").get_text()
        except:
            html = html.decode('gb2312','ignore')
            title = BeautifulSoup(html,'lxml').find("title").get_text()
        title = title[:-19]
        title = title.replace(':', '')
        title = title.replace('?', '')
        title = title.replace('"', '')
        html = urllib.request.urlopen(url).read()
        try:
            htmll = gzip.decompress(html).decode('gb2312','ignore')
            page = BeautifulSoup(htmll, 'lxml').find("span", {"class": "page-ch"}).get_text()
        except:
            html = html.decode('gb2312','ignore')
            page = BeautifulSoup(html, 'lxml').find("span", {"class": "page-ch"}).get_text()
        pattern = re.compile('\d*')
        page = pattern.findall(page)[1]
        os.makedirs(dir + title + page)
    except:
        shutil.rmtree(dir + title + page)
        os.makedirs(dir + title + page)
    try:
        html = urllib.request.urlopen(url).read()
        try:
            htmll = gzip.decompress(html).decode('gb2312','ignore')
            picurl = BeautifulSoup(htmll,'lxml').find("div",{"class": "content-pic"}).find("img")["src"]
        except:
            html = html.decode('gb2312','ignore')
            picurl = BeautifulSoup(html,'lxml').find("div",{"class": "content-pic"}).find("img")["src"]
        req = req_add(picurl)
        img = urllib.request.urlopen(req).read()
        f = open(dir + title + page + "\\" + "1.jpg", "wb")
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
            html = urllib.request.urlopen(url1).read()
            try:
                htmll = gzip.decompress(html).decode('gb2312','ignore')
                picurl = BeautifulSoup(htmll,'lxml').find("div", {"class": "content-pic"}).find("img")["src"]
            except:
                html = html.decode('gb2312','ignore')
                picurl = BeautifulSoup(html,'lxml').find("div", {"class": "content-pic"}).find("img")["src"]
            req = req_add(picurl)
            img = urllib.request.urlopen(req).read()
            f = open(dir + title + page + "\\" + str(i) + ".jpg", "wb")
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