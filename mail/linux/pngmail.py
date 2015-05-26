#!/usr/bin/env python3
#coding: utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

sender = 'itybku@163.com'
receiver = '365474555@qq.com'
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = 'itybku'
password = 'password'

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"

# Create the body of the message (a plain-text and an HTML version).
# 邮件中使用图片的关键是在html页面中引用了图片cid
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.361way.com">运维之路</a> you wanted.
       <font color=red>给我捐赠：<br><img src=\"cid:juanzheng\" border=\"1\">
    </p>
  </body>
</html>
"""

def addimg(src,imgid):
    fp = open(src,'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID',imgid)
    return msgImage


# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

#构造附件
#att = MIMEText(open('h:\\python\\1.jpg', 'rb').read(), 'base64', 'utf-8')
msg.attach(addimg("1.png","juanzheng"))

attach = MIMEText(open('test.xlsx', 'rb').read(), 'base64', 'utf-8')
attach["Content-Type"] = 'application/octet-stream'
# 由于qq邮箱使用gb18030编码，避免乱码这里进行了转码
attach["Content-Disposition"] = 'attachment; filename="测试EXCEL.xlsx"'.decode("utf-8").encode("gb18030")
msg.attach(attach)

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()


