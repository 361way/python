#!/usr/bin/python
#-*- coding: utf-8 -*-
# code from www.361way.com <itybku@139.com>

import os,sys,re,time
import os.path,pexpect

def login_ftp():
    ftp = pexpect.spawn('ftp',cwd=cwd)
    if ftp.expect(prmpt) !=0:
        et cursorlineys.exit()
    ftp.sendline(''.join(('open',ftps)))
	if ftp.expect('Name') != 0:
		sys.exit()
	ftp.sendline(ftpuser)
	if ftp.expect('230') !=0 or ftp.expect(prmpt) !=0:
		sys.exit()
	return ftp

def get_server_files(ftp):
	ftp.sendline('ls')
	if ftp.expect('226') !=0:
		sys.exit()
	filelsts = ftp.before
	filelsts = filelsts.split('\n')
	remtch = re.compile('\s+')
	filelsts = [remtch.subn('',item.strip('\r'))[0] for item in filelsts if
				'group' in item]
	filedict = dict()
	for item in filelsts:
		datas = item.split('')
		filedict[datas[-1]] = {'mon':mons.index(datas[-4]) + 1,'day':int(datas[-3]),'time':datas[-2]}
	return filedict

def get_local_files():
	localfiles = os.listdir(cwd)
	localfilesdict = dict()
	for file in localfiles:
		t = time.ctime(os.stat(os.path.join(cwd,file)).st_mtime)
		datas = t.split('')
		localfilesdict[file] = {'mon':mons.index(datas[-4]) + 1,'day':int(datas[-3]),
		'time':datas[-2][:5]}
	return localfilesdict

def sync_files(ftp,localfilesdict,filedict):
	addfile = []
	for file in localfilesdict.keys():
		if file not in filedict:
			addfile.append(file)
		if file in filedict:
			if localfilesdict[file]['mon'] > filedict[file]['mon'] or localfilesdict[file]['day'] > filedict[file]['day'] or localfilesdict[file]['time'] > filedict[file]['time']:
				addfile.append(file)
	
	delfile = set(filedict.keys()) - set(localfilesdict.keys())
	if addfile:
		for f in addfile:
			ftp.sendline('put' + f)
			if ftp.expect(['226',pexpect.EOF]) ==0:
				print("upload sucess:",f)
			else:
				sys.exit()
	if delfile:
		for f in delfile:
			ftp.sendline('delete' + f)
			if ftp.expect(['250',pexpect.EOF]) == 0:
				print('Del:',f)
			else:
				print('Permission denied!')
				sys.exit()

def exit_ftp(ftp):
	if ftp:
		ftp.sendcontrol('d')
		print(ftp.read().decode())

if __name__ == '__main__':
	mons = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
	cwd = '/home/test'
	prmpt = ['ftp>',pexpect.EOF]
	ftps = '192.168.100.25'
	ftpuser = 'anonymous'
	ftppw = 'abc'
	ftp = login_ftp()
	filedict = get_server_files(ftp)
	localfilesdict = get_local_files()
	sync_files(ftp,localfilesdict,filedict)
	exit_ftp(ftp)

