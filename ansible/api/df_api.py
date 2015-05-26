# cat test_df.py 
#!/usr/bin/env python
# coding=utf-8
import ansible.runner
import json

runner = ansible.runner.Runner(
       module_name='command',
       module_args='df -hl',
       pattern='all',
       forks=10
    )
datastructure = runner.run()
data = json.dumps(datastructure,indent=4)
print data
