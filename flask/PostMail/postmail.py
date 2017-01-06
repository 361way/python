# coding: utf-8
from __future__ import unicode_literals
from email.mime.text import MIMEText
import smtplib

DEFAULT_RECEIVER = ""       # 缺省的邮件接收邮箱
DEFAULT_SENDER_NAME = ""    # 缺省的发送者姓名
MAIL_HOST = ""              # SMTP服务器地址, 如 smtp.126.com
MAIL_ADDRESS = ""           # 服务器登录的邮箱地址
PASSWORD = ""               # 服务器登录的邮箱密码

SECRET_KEY = ""             # 用于验证身份的key, 留空表示不启用key验证机制
AUTO_CC = True              # 对于接收者不包含缺省接收邮箱的请求, 自动抄送一份给缺省邮件接收邮箱, 用于避免接口滥用
RETRY_TIMES = 5             # 邮件发送失败时的自动重试次数
MAIL_PER_CONNECTION = 10    # 每次连接限制发送的邮件数量, 如 126限制每次连接仅可发送10封邮件


class MailSender(object):

    def __init__(self,
                 mail_address=MAIL_ADDRESS,
                 password=PASSWORD,
                 mail_host=MAIL_HOST,
                 sender=DEFAULT_SENDER_NAME,
                 default_receiver=DEFAULT_RECEIVER,
                 key=SECRET_KEY,
                 auto_cc=AUTO_CC,
                 retry=RETRY_TIMES,
                 mail_per_connection=MAIL_PER_CONNECTION):

        self.mail_address = mail_address
        self.password = password
        self.mail_host = mail_host
        self.sender_name = sender
        self.default_receiver = default_receiver
        self.server = smtplib.SMTP()
        self.secret_key = key
        self.auto_cc = auto_cc
        self.retry = retry
        self.mails_sent_in_current_connection = 0
        self.mail_per_connection = mail_per_connection
        self.login()

    def login(self):
        print("Trying to connect smtp server")
        self.server.connect(self.mail_host)
        self.server.login(self.mail_address, self.password)
        print("SMTP server login successfully.")

    def logout(self):
        self.server.close()

    def send(self, subject, content, sender_name=None, receiver=None, cc=None, bcc=None, subtype='plain', **kwargs):
        """
        simply send a email with subject and content.

        :type subject:     str
        :type content:     str
        :type sender_name: str
        :type receiver:    str or list
        :type cc:          str or list
        :type bcc:         str or list
        :type subtype      enumerate 'plain' or 'html'
        :return:           None
        """

        if self.secret_key and kwargs.get('key') != self.secret_key:
            raise KeyError("Invalid key")
        if len(content) == 0:
            raise ValueError("Empty Content")

        _sender_name =  sender_name or self.sender_name
        _receiver =     convert_to_list(receiver or self.default_receiver)
        _cc =           convert_to_list(cc)
        _bcc =          convert_to_list(bcc)

        if self.auto_cc is True and self.default_receiver not in _receiver + _cc + _bcc:
            _cc.append(self.default_receiver)

        mail_str = self.build_mail_str(subject=subject, content=content, sender=_sender_name, receiver=_receiver,
                                       cc=_cc, bcc=_bcc, subtype=subtype)

        fail_times = 0
        while fail_times < self.retry:
            try:
                self.server.sendmail(self.mail_address, _receiver, mail_str)
                self.mails_sent_in_current_connection += 1
                break
            except Exception:
                fail_times += 1
                self.logout()
                self.login()

        if fail_times >= self.retry:
            raise IOError('Mail sending failed.')

        if self.mails_sent_in_current_connection >= self.mail_per_connection:
            self.logout()
            self.login()

    def build_sender_str(self, sender_name):
        if sender_name:
            return "{0}<{1}>".format(sender_name, self.mail_address)
        else:
            return None

    def build_mail_str(self, subject, content, sender, receiver, cc, bcc, subtype='plain'):
        mail = MIMEText(content, _subtype=subtype, _charset='utf-8')

        mail['Subject'] = subject
        mail['From'] = self.build_sender_str(sender)

        mail['To'] = "; ".join(receiver)
        mail['Cc'] = "; ".join(cc)
        mail['Bcc'] = "; ".join(bcc)

        return mail.as_string()


def convert_to_list(obj):
    if obj:

        if isinstance(obj, unicode):
            return [obj]
        elif isinstance(obj, list):
            return obj
        else:
            print(obj)
            raise TypeError("Only accept unicode or list as parameter, given: {}".format(type(obj)))

    else:

        return []
