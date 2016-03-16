#!/usr/bin/env python
# coding=utf-8
# site: www.361way.com   
# mail: itybku@139.com
# desc: Rotating logfile by times or size


import re
import subprocess
import logging
import socket,time
from logging.handlers import TimedRotatingFileHandler

LOG_FILE = "/var/log/ping/ping.log"

#logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',datefmt='%Y-%m-%d %I:%M:%S',filemode='w')   #for term print
logger = logging.getLogger()
logger.setLevel(logging.INFO)
fh = TimedRotatingFileHandler(LOG_FILE,when='M',interval=1,backupCount=30)
datefmt = '%Y-%m-%d %H:%M:%S'
format_str = '%(asctime)s %(levelname)s %(message)s '
#formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
formatter = logging.Formatter(format_str, datefmt)
fh.setFormatter(formatter)
logger.addHandler(fh)
#logging.info(msg)
#hdlr.flush()

#----------------------------------------------------------------------
def pinghost(host):
    ping = subprocess.Popen(["ping", "-c", "1",host],stdout = subprocess.PIPE,stderr = subprocess.PIPE)
    out, error = ping.communicate()
    if "icmp_seq" in  out:
        icmp_line = re.findall(r'\d+\sbytes(.*?)ms',out)
        logging.info('ping ' + host + str(icmp_line))
    else:
        logging.info('ping ' + host + ' fail')
        
        
def tcping(server, port):
    ''' Check if a server accepts connections on a specific TCP port '''
    try:
        start = time.time()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server, port))
        s.close()
        #print server + ':' + str(port) + '/tcp - ' +  str(port) + ' port is open' + ' - time=' + str(round((time.time()-start)*10000)/10) + 'ms'
        msg = server + ':' + str(port) + '/tcp - ' +  str(port) + ' port is open' + ' - time=' + str((time.time()-start)*1000) + 'ms'
        logging.info(msg)
    except socket.error:
        msg = server + ':' + str(port) + ' port not open'
        logging.info(msg)

while 1:
    pinghost('passport.migu.cn')
    pinghost('112.17.9.72')
    tcping('passport.migu.cn',8443)
    tcping('112.17.9.72',8443)
    #time.sleep(0.5)

