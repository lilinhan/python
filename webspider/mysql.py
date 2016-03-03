#!/usr/bin/env python
# encoding: utf-8

import MySQLdb

db = MySQLdb.connect('localhost', 'root', 'lewin123', 'moviedb')
cursor = db.cursor()

sql = """INSERT INTO movie_data(name, picture, classfication, area, year, director, star,
        score, summary, download, jpg) VALUES('1','2','3','4','5','6','7','8','9','10','11')"""

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
