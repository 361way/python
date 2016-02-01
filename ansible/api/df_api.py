#!/usr/bin/env python
# coding=utf-8
## site: www.361way.com
## mail: itybku@139.com
## desc: get more then 30% mount point of all hosts

import ansible.runner
#import json
runner = ansible.runner.Runner(
           module_name='shell',
           module_args="df -hP|awk 'NR>1 && int($5)>30'",
           pattern='all',
           forks=10
        )
results = runner.run()
#print  results
for (hostname, result) in results['contacted'].items():
    if not 'failed' in result:
        for line in  result['stdout'].split('\n'):
            print "%s  %s" % (hostname, line)


