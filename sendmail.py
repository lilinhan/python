#!/usr/bin/env python
# encoding: utf-8

import smtplib

smtpServer = 'smtp.qq.com'
fromaddr = '693465363@qq.com'
toaddr = '869780307@qq.com'
msg = 'Subject:hello world!'
server = smtplib.SMTP(smtpServer)
server.sendmail(fromaddr, toaddr, msg)
server.quit()

