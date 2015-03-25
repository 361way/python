import sys
import time
import urllib3
#url = "http://www.361way.com/python-mysqldb/3842.html"
url = "http://blog.linuxeye.com/sitemap.html"
now = time.time()
pool = urllib3.PoolManager()
r = pool.request('GET', url, assert_same_host=False)
elapsed = time.time() - now
print r.data , elapsed
