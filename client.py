#!/usr/bin/env python
# encoding: utf-8

import socket
Host = '127.0.0.1'
Port = 9999

request = 'Can you hear me?'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
s.connect((Host,Port))

s.sendall(request)

reply = s.recv(1024)

print 'reply is: ', reply

s.close()
