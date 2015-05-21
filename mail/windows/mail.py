# -*- coding: cp936 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mailto_list=['365474555@qq.com','itybku@139.com']
mail_host="smtp.163.com"  #设置服务器
mail_user="itybku"     #用户名
mail_pass="password"    #口令 
mail_postfix="163.com"  #发件箱的后缀

def send_mail(to_list,sub,content):
    me="itybku@163.com"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,'plain',_charset='gb2312')
    msg['Subject'] = Header(sub,"gb2312")
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    if send_mail(mailto_list,"标题！","正常文！"):
        print "发送成功"
    else:  
        print "发送失败"

