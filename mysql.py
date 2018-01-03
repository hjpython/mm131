import pymysql
url = 'hao'
conn = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='mypydb',charset='utf8')
cur = conn.cursor()
sql = ("insert into mm131m(url)" "values(%s)")
cur.execute(sql,url)
conn.commit()
cur.close()
conn.close()