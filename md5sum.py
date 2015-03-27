#!/usr/bin/python
#encoding=utf-8
import io
import sys
import hashlib
import string

def printUsage():
	print ('''Usage: [python] pymd5sum.py <filename>''')
	
def main():
	if(sys.argv.__len__()==2):
		#print(sys.argv[1])

		m = hashlib.md5()
		file = io.FileIO(sys.argv[1],'r')
		bytes = file.read(1024)
		while(bytes != b''):
			m.update(bytes)
			bytes = file.read(1024) 
		file.close()
		
		#md5value = ""
		md5value = m.hexdigest()
		print(md5value+"\t"+sys.argv[1])
		
		#dest = io.FileIO(sys.argv[1]+".CHECKSUM.md5",'w')
		#dest.write(md5value)
		#dest.close()
	
	else:
		printUsage() 
main()
