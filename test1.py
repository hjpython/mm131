#!/usr/bin/env python
# coding=utf-8
import urllib.request
from bs4 import BeautifulSoup
import os
import shutil
import urllib.error
import pymysql
url = 'http://www.mm131.com/xinggan/'
html = urllib.request.urlopen(url).read()
urls = BeautifulSoup(html,'lxml').find('dl',{'class':'list-left public-box'}).findAll('a',{'target':'_blank'})
for url in urls:
    url = url['href']
    print(url)