#!/usr/bin/env python
# encoding: utf-8

import sys, urllib, urllib2, json

str = raw_input("what do you want?\n")
while(str != '#'):
    targetfront = "http://apis.baidu.com/apistore/tranlateservice/translate?query="
    #str = raw_input("what do you want?\n")
    str = urllib.quote(str)
    targetrear = "&from=en&to=zh"

    url = targetfront + str + targetrear

    req = urllib2.Request(url)

    req.add_header("apikey", "40cc7baa214cf97ad227585ab10b0fbb")

    resp = urllib2.urlopen(req)
    content = resp.read()
    if(content):
        s = json.loads(content);
        #print(content)
    print s["retData"]["trans_result"][0]["dst"]
    str = raw_input("what do you want?\n")
