#!/usr/bin/env python
# coding:utf8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

msg = MIMEMultipart('alternative')
text = '''
\n
内容服务器目前总的disk空间使用情况和inode使用情况见附件：summary.txt 
空间使用超过80%的挂载点见附件：alarmdisk.txt 
inode使用空间超过80%挂载点见附件：alarminode.txt 
'''
if isinstance(text,unicode):
   text = str(text)

part1 = MIMEText(text, 'plain','utf-8')
msg.attach(part1)

att1 = MIMEText(open('/tmp/summary.txt', 'rb').read(), 'base64', 'utf8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="summary.txt"'
msg.attach(att1)

att2 = MIMEText(open('/tmp/alarmdisk', 'rb').read(), 'base64', 'utf8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="alarmdisk.txt"'
msg.attach(att2)

att3 = MIMEText(open('/tmp/alarminode', 'rb').read(), 'base64', 'utf8')
att3["Content-Type"] = 'application/octet-stream'
att3["Content-Disposition"] = 'attachment; filename="alarminode.txt"'
msg.attach(att3)

subject = '内容服务器磁盘和inode巡检结果'
if not isinstance(subject,unicode):
   subject = unicode(subject)

msg['to'] = 'itybku@139.com'
msg['from'] = 'itybku@163.com'
msg['subject'] = subject
msg["Accept-Language"]="zh-CN"
msg["Accept-Charset"]="ISO-8859-1,utf-8"

try:
    server = smtplib.SMTP()
    server.connect('smtp.163.com')
    server.login('itybku','mypassword')
    server.sendmail(msg['from'], msg['to'],msg.as_string())
    server.quit()
    print '发送成功'
except Exception, e:
    print str(e)
