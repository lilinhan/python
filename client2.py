#!/usr/bin/env python
# encoding: utf-8

import socket,os
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.connect(('127.0.0.1', 8123))

ss.sendall('wo kao sile')
os.system('sleep 1')
ss.send('FOE')
data = ss.recv(1024)
print "Server dafu %s" %data
ss.close()
