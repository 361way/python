#/bin/bash
# author : www.361way.com
IP=`ip add show|grep inet|grep 10|awk '{print $2}'`
df -hl|grep '^/'|sed 's/%//g'|awk '{if($5>30) print $0}'|while read line
do
    echo $IP `hostname` $line
done