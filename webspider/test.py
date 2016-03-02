#!/usr/bin/env python
# encoding: utf-8

from bs4 import BeautifulSoup  #解析Dom
import urllib2

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

def print_url_list(urllist):
    for li in urllist:
        print li

def loop_all_page():
    urllist = []
    url = 'http://www.xunleigang.com/forum.php?mod=forumdisplay&fid=2&ortid=1&page='
    for i in range(1,3):
        url += str(i)
        get_url_list_in_one_page(url,urllist)

    print_url_list(urllist)

if __name__ == '__main__' :
    loop_all_page()
