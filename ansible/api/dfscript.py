#!/usr/bin/env python
# coding=utf-8
## author : www.361way.com
## mail : itybku@139.com
## desc : get host(IP  hostname  mount point use)
import ansible.runner
#import json
runner = ansible.runner.Runner(
           module_name='script',
           module_args="aa.sh",
           pattern='all',
           forks=10
        )
results = runner.run()
#print  results
for (hostname, result) in results['contacted'].items():
    if not 'failed' in result:
        for line in  result['stdout'].split('\r\n'):
            #print "%s  %s" % (hostname, line)
            print lin