#!/usr/bin/env python
# encoding: utf-8

from bs4 import BeautifulSoup  #解析Dom
import urllib2
import time
import MySQLdb

def get_movie_info(url, jpg):
    db = MySQLdb.connect('localhost', 'root', 'lewin123', 'moviedb')
    cursor = db.cursor()
    path = 'http://www.xunleigang.com/'
    list = []
    req = urllib2.Request(path+url)
    req.add_header('User-agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36')
    res = urllib2.urlopen(req)
    soup = BeautifulSoup(res)


#get movie name
    name_html = soup.find('caption')
    movie_name = name_html.get_text()[:name_html.get_text().find(':')]
    #print movie_name
#get movie info
    info_html = soup.find('tbody')
    for child in info_html.children:
        if not child.find('_blank'):
            list.append(child.td.get_text())

#get movie content
#download address = url
#jpg = jpg
    jpg = path + jpg

    sql = """INSERT INTO movie_data(name, picture, classfication, area, year, director, star,
        score, download, jpg) VALUES(movie_name,list[1],list[2],list[3],list[4],list[5],list[6],path+url,jpg)"""
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

    print movie_name

def get_url_list_in_one_page(url, urllist):
    req = urllib2.Request(url)
    req.add_header('User-agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36')

    res = urllib2.urlopen(req)

    soup = BeautifulSoup(res)
    for link in soup.find_all('a'):
        if 'target' in link.attrs.keys() and 'title' in link.attrs.keys() and 'class' in link.attrs.keys():
            #print link.attrs
            if not link.attrs['href'].find('thread') :
                urllist.append(link.attrs['href'])
                #print link.img.attrs['src']
                get_movie_info(link.attrs['href'], link.img.attrs['src'])

def print_url_list(urllist):
    for li in urllist:
        print li

def loop_all_page():
    urllist = []
    url = 'http://www.xunleigang.com/forum.php?mod=forumdisplay&fid=2&ortid=1&page='
    for i in range(1,265):
        url += str(i)
        get_url_list_in_one_page(url,urllist)

    #print_url_list(urllist)


if __name__ == '__main__' :
    loop_all_page()
