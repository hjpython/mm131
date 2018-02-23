import urllib.request
import pymysql

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
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='mypydb', charset='utf8')
    cur = conn.cursor()
    sql = ("insert into mm131(url)" "values(%s)")
    cur.execute(sql, url)
    conn.commit()
    cur.close()
    conn.close()