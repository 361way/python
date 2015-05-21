# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
import os
import sys

def send_mail(subject, body, mail_to, username, password, mail_type='plain'):
    assert isinstance(mail_to, list) == True
    msg = MIMEText(body,'html',_charset='UTF-8')
    # 定义标题
    msg['Subject'] = Header(subject,"UTF-8")
    # 定义发信人
    msg['From'] = username
    # 
    msg['To'] = ';'.join(mail_to)
    # 定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    try:
        smtp = smtplib.SMTP()
        # 连接SMTP服务器，
        smtp.connect('smtp.163.com')
        # 用户名密码
        smtp.login(username, password)
        smtp.sendmail(username, mail_to, msg.as_string())
        smtp.quit()
        return True
    except Exception as e:
        print "send mail error:%s"%e
        return False

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print 'Usage : python mail.py object_mail'
        sys.exit()

    subject = '你好，这是一封测试邮件'
    body = '''
这是经过我们的python程序发送的一封邮件，请勿直接回复
    '''
    mail_to = [sys.argv[1]]
    username = 'itybku@163.com'
    #password = os.getenv('PASSWORD')
    password = 'password'
    send_mail(subject, body, mail_to, username, password)
