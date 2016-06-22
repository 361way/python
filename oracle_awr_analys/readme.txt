功能介绍：读取AWR文件获取数据存入ORACLE数据库（Load Profile，Instance
Efficiency，Foreground Wait Events，SQL Statistics）
测试环境：python 2.6 ,cx_oracle5.1, AWR File(11.1.0.7.0)
模块介绍：
awr_main.py
主程序

awr_regular.py
通过正则表达式获取数据

awr_db.py
判读AWR文件是否分析过；
保持分析的结果（Load Profile，Instance Efficiency，等）到数据库

awr_backup.py
被awr_db.py调用，把分析完的AWR备份

awr_constant.py
一些预先定义的正则表达式和SQL语句

awr_configure.py
配置信息，包括AWR读取的路径，备份目录（可选项），日志文件等

create_awr.sql
DB表结构

数据库

eg:日志输出



