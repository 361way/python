#!/usr/bin/env python
#-*- encoding: utf-8 -*-
#


import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email(title = '软件监控通知邮件',meial_server = '',from_name = '', from_pwd = '' ,to_name_list=[],message=''):
    msg = MIMEText(message,'html',_charset='UTF-8') #设置UTF-8编码
    msg['Subject'] =Header(title,"UTF-8")           #设置UTF-8编码
    msg['From'] = meial_server
    msg['To'] = ";".join(to_name_list)
    #print msg
    try:
        s = smtplib.SMTP()
        s.connect(meial_server)
        s.login(from_name,from_pwd)
        s.sendmail(from_name, to_name_list, msg.as_string()) 
        return True
    except Exception, e:
        print str(e)
        return False
    finally:
        s.close()

    
if __name__=="__main__":
    print send_email(title='软件监控通知邮件',meial_server='smtp.163.com',from_name='itybku@163.com',from_pwd='password',to_name_list=['365474555@qq.com','itybku@139.com'],message='恭喜您，邮件发送成功！')
