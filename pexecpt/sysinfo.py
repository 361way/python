#!/usr/bin/python
#-*- coding: utf-8 -*-
# code from www.361way.com <itybku@139.com>

from pexpect.pxssh import pxssh
import pexpect

def login_host(host):
	s = pxssh()
	if s.login(host[0],host[1],host[2]):
		return s

def get_cpus(sshc):
	sshc.sendline('cat /proc/cpuinfo')
	res = sshc.expect(['cpu cores.*\r\n',pexpect.EOF])
	if res == 0:
		data = sshc.after.decode().split('\r\n')
		data = data[0]
		data = data[data.index(':') + 1:]
		cpucores = int(data)
		sshc.prompt()
		return cpucores


def get_cpu_load(sshc):
	sshc.sendline('uptime')
	if sshc.prompt():
		data = sshc.after.decode()
		data = data.strip('\r\n')
		data = data[data.rfind(':') + 1:]
		data = data.split(',')
		return (float(data[0]),float(data[1]),float(data[2]))

def get_cpu_stat(sshc):
	sshc.sendline('vmstat')
	sshc.prompt()
	print(sshc.before.decode())

def user_deal(host,logfilename):
	s = login_host(host)
	if not s:
		print("login failure:",host[0])
		return
	try:
		cpucores = get_cpus(s)
		if not cpucores:
			print("Do not get cpucores:",host[0])
			return
		cpu_load = get_cpu_load(s)
		if cpu_load[2] >= cpucores:
			get_cpu_stat(s)
			print("System is not healthy.Do you want to deal?(yes/no)")
			yn = input()
			if yn == 'yes':
				with open(logfilename,'ab+') as f:
					s.logfile = f
					s.interact()
					s.prompt()
					s.logfile = None
		else:
			print("System is healthy:",host[0])
	except:
		print('Failure:',host[0])
	finally:
		s.logout()

if __name__ == '__main__':
	hosts = [('192.168.1.22','root','123456'),]
	logfilename = 'log.txt'
	for host in hosts:
		user_deal(host,logfilename)

