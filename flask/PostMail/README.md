# PostMail
一个让你能够使用 POST 请求发送邮件的简易 Flask Server

[English Ver. README](#eng_title)

# 快速开始

0. 安装 Flask

    ```bash
    sudo pip install Flask
    ```
1. 在 **postmail.py** 开头配置必要参数

    ```python
    DEFAULT_RECEIVER = ""       # 缺省的邮件接收邮箱
    DEFAULT_SENDER_NAME = ""    # 缺省的发送者姓名
    MAIL_HOST = ""              # SMTP服务器地址, 如 smtp.126.com
    MAIL_ADDRESS = ""           # 服务器登录的邮箱地址
    PASSWORD = ""               # 服务器登录的邮箱密码
    ```
2. 运行服务器，默认运行在 80 端口以及对应 url 是 '/mail'

    ```bash
    python run.py
    ```
3. 然后就可以用 POST 请求发邮件了！ 你甚至不需要指定收件人，因为配置里有『默认收件人』这一选项

    ```python
    import requests

    response = requests.post('http://www.yourserver.com/mail', data={
        'subject': "PostMail!",
        'content': "This mail is sent by PostMail!"
    })
    ```

# 高级

- 使用安全密钥来提升安全性
    修改**postmail.py**文件开头的秘钥选项

    ```python
    SECRET_KEY = "your_key"             # 用于验证身份的key, 留空表示不启用key验证机制
    ```
    然后你的所有请求都必须包含正确的key才会被执行发送

    ```python
    import requests

    response = requests.post('http://www.yourserver.com/mail', data={
        'key': "your_key",
        'subject': "PostMail!",
        'content': "This mail is sent by PostMail!"
    })
    ```

- HTML 邮件支持
    你能使用 PostMail 来发送HTML邮件, 只需要在请求中附带 `'subtype'` 参数并设置为 `'html'`即可。这一选项默认为 `'plain'`

    ```python
    import requests

    response = requests.post('http://www.yourserver.com/mail', data={
        'subtype': "html",
        'subject': "PostMail!",
        'content': "This mail is sent by PostMail!"
    })
    ```

<h1 id='eng_title'> PostMail </h1>
A simple mail server which can let you send a email only sending a POST request

# Quick start

0. install Flask

    ```bash
    sudo pip install Flask
    ```
1. set up the configurations at the beginning of **postmail.py**

    ```python
    DEFAULT_RECEIVER = ""       # 缺省的邮件接收邮箱
    DEFAULT_SENDER_NAME = ""    # 缺省的发送者姓名
    MAIL_HOST = ""              # SMTP服务器地址, 如 smtp.126.com
    MAIL_ADDRESS = ""           # 服务器登录的邮箱地址
    PASSWORD = ""               # 服务器登录的邮箱密码
    ```
2. run the server, the server is default running on port 80 and set on url of '/mail'.

    ```bash
    python run.py
    ```
3. **use POST to send the mail!**
    you don't even need to set the mail receiver!

    ```python
    import requests

    response = requests.post('http://www.yourserver.com/mail', data={
        'subject': "PostMail!",
        'content': "This mail is sent by PostMail!"
    })
    ```

# Requirement
- Flask

# Advance

- Use a key to enhance security
    modify the string at the beginning of **postmail.py**

    ```python
    SECRET_KEY = "your_key"             # 用于验证身份的key, 留空表示不启用key验证机制
    ```
    Then all the request must contain the valid key as parameter

    ```python
    import requests

    response = requests.post('http://www.yourserver.com/mail', data={
        'key': "your_key",
        'subject': "PostMail!",
        'content': "This mail is sent by PostMail!"
    })
    ```

- HTML mail support
    you can use PostMail to send HTML mail by setting 'subtype' as 'html', which is default set to 'plain'

    ```python
    import requests

    response = requests.post('http://www.yourserver.com/mail', data={
        'subtype': "html",
        'subject': "PostMail!",
        'content': "This mail is sent by PostMail!"
    })
    ```

# License
MIT

