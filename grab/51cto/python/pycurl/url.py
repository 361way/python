import pycurl
import StringIO
 
url = "http://www.361way.com/python-mysqldb/3842.html"
crl = pycurl.Curl()
crl.setopt(pycurl.USERAGENT,"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0)")  
crl.setopt(pycurl.VERBOSE,1)
crl.setopt(pycurl.FOLLOWLOCATION, 1)
crl.setopt(pycurl.MAXREDIRS, 5)
crl.fp = StringIO.StringIO()
crl.setopt(pycurl.URL, url)
crl.setopt(crl.WRITEFUNCTION, crl.fp.write)
crl.perform()
print crl.fp.getvalue()
