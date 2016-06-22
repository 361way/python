export ORACLE_BASE=/opt/oracle
export ORACLE_HOME=$ORACLE_BASE/product/11gR1/db
export LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib:$ORACLE_HOME/rdbms/lib

/home/oracle/sj/python2.7/bin/python /home/oracle/sj/awr_analysed/bin/awr_main.py

