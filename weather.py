#!/usr/bin/env python
# encoding: utf-8

import sys, urllib, urllib2, json

url = 'http://apis.baidu.com/heweather/weather/free?city='

str = raw_input("你想查询哪个城市的天气状况?\n")
url += str

req = urllib2.Request(url)

req.add_header("apikey", "40cc7baa214cf97ad227585ab10b0fbb")

resp = urllib2.urlopen(req)
content = resp.read()

if(content):
    str = json.loads(content)
    #print(content)

print str["HeWeather data service 3.0"][0]["basic"]["cnty"] + str["HeWeather data service 3.0"][0]["basic"]["city"]
print "当地时间: "
print str["HeWeather data service 3.0"][0]["basic"]["update"]["loc"]
print "天气: "
print str["HeWeather data service 3.0"][0]["now"]["cond"]["txt"]
print "温度"
print str["HeWeather data service 3.0"][0]["now"]["tmp"]
print "体感温度"
print str["HeWeather data service 3.0"][0]["now"]["fl"]
print "相对湿度"
print str["HeWeather data service 3.0"][0]["now"]["hum"]
print "降水量"
print str["HeWeather data service 3.0"][0]["now"]["pcpn"]
print "气压"
print str["HeWeather data service 3.0"][0]["now"]["pres"]
print "空气质量指数"
print str["HeWeather data service 3.0"][0]["aqi"]["city"]["aqi"]
print "PM2.5 1小时平均值"
print str["HeWeather data service 3.0"][0]["aqi"]["city"]["pm25"]
print "PM10 1小时平均值"
print str["HeWeather data service 3.0"][0]["aqi"]["city"]["pm10"]
print "空气质量类别"
print str["HeWeather data service 3.0"][0]["aqi"]["city"]["qlty"]
print "舒适度指数"
print str["HeWeather data service 3.0"][0]["suggestion"]["comf"]["brf"] + str["HeWeather data service 3.0"][0]["suggestion"]["comf"]["txt"]
print "洗车指数"
print str["HeWeather data service 3.0"][0]["suggestion"]["cw"]["brf"] + str["HeWeather data service 3.0"][0]["suggestion"]["cw"]["txt"]
print "穿衣指数"
print str["HeWeather data service 3.0"][0]["suggestion"]["drsg"]["brf"] + str["HeWeather data service 3.0"][0]["suggestion"]["drsg"]["txt"]
print "感冒指数"
print str["HeWeather data service 3.0"][0]["suggestion"]["flu"]["brf"] + str["HeWeather data service 3.0"][0]["suggestion"]["flu"]["txt"]
print "运动指数"
print str["HeWeather data service 3.0"][0]["suggestion"]["sport"]["brf"] + str["HeWeather data service 3.0"][0]["suggestion"]["sport"]["txt"]
print "旅游指数"
print str["HeWeather data service 3.0"][0]["suggestion"]["trav"]["brf"] + str["HeWeather data service 3.0"][0]["suggestion"]["trav"]["txt"]
print "紫外线指数"
print str["HeWeather data service 3.0"][0]["suggestion"]["uv"]["brf"] + str["HeWeather data service 3.0"][0]["suggestion"]["uv"]["txt"]

