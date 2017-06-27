#!/bin/bash
TIME=`date +'%F %T'`
ansible -i /etc/ansible/hosts httpcontent -m raw -a 'df -hP' >  /tmp/httpcontent.txt
ansible -i /etc/ansible/hosts httpcontent -m raw -a 'df -iP' >  /tmp/httpinode.txt
echo '****************************************************' > /tmp/summary.txt
echo '          http coutent disk use count               ' >> /tmp/summary.txt
echo '****************************************************' >> /tmp/summary.txt
grep ':/' /tmp/httpcontent.txt  |column -t|sort|uniq >> /tmp/summary.txt


echo '****************************************************' >> /tmp/summary.txt
echo '          http coutent inode use count              ' >> /tmp/summary.txt
echo '****************************************************' >> /tmp/summary.txt
grep ':/' /tmp/httpinode.txt  |column -t|sort|uniq >> /tmp/summary.txt

grep ':/' /tmp/httpcontent.txt  |column -t|sort|uniq|awk 'int($(NF-1)) > 80' > /tmp/alarmdisk
grep ':/' /tmp/httpinode.txt  |column -t|sort|uniq|awk 'int($(NF-1)) > 80' > /tmp/alarminode


python sendPmail.py
echo "create time $TIME" >> /tmp/httpcontent.txt
echo "create time $TIME" >> /tmp/httpinode.txt
