#!-*- encoding: utf-8 -*- 
import urllib2
import logging 
import os 
import time 
from ConfigParser import ConfigParser
from logging.handlers import TimedRotatingFileHandler

LOG_FILE = "./logs/output.log"

logger = logging.getLogger()
logger.setLevel(logging.INFO)
fh = TimedRotatingFileHandler(LOG_FILE,when='midnight',interval=1,backupCount=30)
datefmt = '%Y-%m-%d %H:%M:%S'
format_str = '%(asctime)s %(levelname)s %(message)s '
formatter = logging.Formatter(format_str, datefmt)
fh.setFormatter(formatter)
fh.suffix = "%Y%m%d%H%M"
logger.addHandler(fh)

def getUrlcode(url):
    try:
        start = time.time()
        response = urllib2.urlopen(url,timeout=10)
        msg = 'httpcode is ' + str(response.getcode()) + ' - open url use time ' + str((time.time()-start)*1000) + 'ms'
        logging.info(msg)
        return response.getcode()
    except urllib2.URLError as e:
        msg = 'open url error ,reason is:' + str(e.reason) 
        logging.info(msg)

def get(field, key):
    result = ""
    try:
        result = cf.get(field, key)
    except:
        result = ""
    return result
    
def read_config(config_file_path, field, key): 
    cf = ConfigParser()
    try:
        cf.read(config_file_path)
        result = cf.get(field, key)
    except:
        sys.exit(1)
    return result

CONFIGFILE='./cfg/config.ini' 

os.environ["JAVA_HOME"] = read_config(CONFIGFILE,'MonitorProgram','JAVA_HOME')
os.environ["CATALINA_HOME"] = read_config(CONFIGFILE,'MonitorProgram','CATALINA_HOME')

ProgramPath = read_config(CONFIGFILE,'MonitorProgram','StartPath') 
ProcessName = read_config(CONFIGFILE,'MonitorProcessName','ProcessName')
url = read_config(CONFIGFILE,'MonitorUrl','Url')
#url = "http://dh.361way.com/"


while True:
    HttpCode = getUrlcode(url)

    if HttpCode is not 200:
         command = 'taskkill /F /FI "WINDOWSTITLE eq ' + ProcessName + '"'
         os.system(command)
         os.system(ProgramPath)

    time.sleep(30)

'''
import os
import socket
def IsOpen(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((ip,int(port)))
        s.shutdown(2)
        print '%d is open' % port
        return True
    except:
        print '%d is down' % port
        return False
if __name__ == '__main__':
    IsOpen('127.0.0.1',800) '''
