#!/usr/bin/env python

#
awr_file = '/home/oracle/sj/awr_analysed/awr'

#
backup_dir='/home/oracle/sj/awr_analysed/backup'

#
awr_log='/home/oracle/sj/awr_analysed/awr_logs.log'


#
num_wait_event = 10

#
debug_flag=1
#
oracle_username='awr'
oracle_password='awr'
oracle_tnsnames='''
(DESCRIPTION =
       (ADDRESS = (PROTOCOL = TCP)(HOST = 10.211.93.147)(PORT = 1521))
     (CONNECT_DATA =
             (SERVER = DEDICATED)
             (SERVICE_NAME = orcl)
            (INSTANCE_NAME = orcl2)
     )
 )
 '''
 
#define sql
insert_stat_value ="insert into load_profile(dbid,instance_name,begin_date,end_date,begin_snap_id,end_snap_id,\
db_time_s ,db_cpu_s,redo_size_s,\
logical_read_s,block_chagnes_s,physical_read_s,\
physical_write_s,user_call_s,parse_s,\
hard_parse_s,wa_mb_processed_s,logons_s,\
executes_s,rollbacks_s,transactions_s) \
values(:dbid,:instance_name,:begin_date,:end_date,:begin_snap_id,:end_snap_id,\
:db_time_s ,:db_cpu_s,:redo_size_s,\
:logical_read_s,:block_chagnes_s,:physical_read_s,\
:physical_write_s,:user_call_s,:parse_s,\
:hard_parse_s,:wa_mb_processed_s,:logons_s,\
:executes_s,:rollbacks_s,:transactions_s)"

insert_efficiency_value= "insert into inst_efficiency(instance_name,dbid,begin_date,end_date,begin_snap_id ,end_snap_id ,\
buffer_nowait ,redo_nowait , buffer_hit ,\
InMemory_sort ,library_hit , soft_parse , \
exec_parse ,latch_hit , parseCPU_parseElapsd ,\
nonParse_CPU ,user_cpu, sys_cpu, wio_cpu, idle_cpu ) \
values(:instance_name,:dbid,:begin_date,:end_date,:begin_snap_id ,:end_snap_id ,\
:buffer_nowait ,:redo_nowait , :buffer_hit ,\
:InMemory_sort ,:library_hit , :soft_parse , \
:exec_parse ,:latch_hit , :parseCPU_parseElapsd ,\
:nonParse_CPU ,:user_cpu, :sys_cpu, :wio_cpu, :idle_cpu )"

insert_waitEvent_value= "insert into wait_events(instance_name ,dbid,begin_date,end_date,begin_snap_id ,end_snap_id ,\
wait_name  , waits, time_outs , total_wait_time ,\
avg_wait_time , waits_txn , wait_db_time ) \
values(:instance_name ,:dbid,:begin_date,:end_date,:begin_snap_id ,:end_snap_id ,\
:wait_name  , :waits, :time_outs , :total_wait_time ,\
:avg_wait_time , :waits_txn , :wait_db_time )"

insert_sqlid_elapsed_time= "insert into sql_elapsed_time(instance_name ,dbid,begin_date,\
                            end_date,begin_snap_id ,end_snap_id   ,\
                            elapsed_time ,cpu_time ,executions ,\
                            elap_per_exec ,total_db_time ,sql_id)\
values(:instance_name ,:dbid,:begin_date,\
       :end_date,:begin_snap_id ,:end_snap_id   ,\
       :elapsed_time ,:cpu_time ,:executions ,\
       :elap_per_exec ,:total_db_time ,:sql_id)"    

insert_sqlid_cpu_time = "insert into sql_cpu_time(instance_name ,dbid,begin_date,end_date,begin_snap_id ,\
                        end_snap_id ,cpu_time ,elapsed_time  ,executions ,cpu_per_exec ,\
                        total ,total_db_time ,sql_id )\
values(:instance_name ,:dbid,:begin_date,:end_date,:begin_snap_id ,\
:end_snap_id ,:cpu_time ,:elapsed_time  ,:executions ,:cpu_per_exec ,\
:total ,:total_db_time ,:sql_id )"

insert_sql_id_buffer_gets = "insert into sql_buffer_gets(  instance_name ,dbid,begin_date,\
                            end_date,begin_snap_id,end_snap_id  ,buffer_gets ,executions ,\
                            gets_per_exec ,total ,cpu_time ,elapsed_time ,sql_id )\
values(:instance_name ,:dbid,:begin_date,\
:end_date,:begin_snap_id,:end_snap_id  ,:buffer_gets ,:executions ,\
:gets_per_exec ,:total ,:cpu_time ,:elapsed_time ,:sql_id )"

insert_sqlid_physical_read = "insert into sql_physical_read(instance_name ,dbid,begin_date,end_date ,\
begin_snap_id ,end_snap_id   ,physical_read  ,executions  ,reads_per_exec  ,total  ,\
cpu_time  ,elapsed_time  ,sql_id ) \
values(:instance_name ,:dbid,:begin_date,:end_date ,\
:begin_snap_id ,:end_snap_id   ,:physical_read  ,:executions  ,:reads_per_exec  ,:total  ,\
:cpu_time  ,:elapsed_time  ,:sql_id )"

insert_sqlid_executions = "insert into sql_executions(instance_name,dbid,begin_date,end_date,\
begin_snap_id ,end_snap_id,executions ,row_processed ,rows_per_exec ,\
cpu_per_exec ,elap_per_exec ,sql_id  )\
values(:instance_name,:dbid,:begin_date,:end_date,\
:begin_snap_id ,:end_snap_id,:executions ,:row_processed ,:rows_per_exec ,\
:cpu_per_exec ,:elap_per_exec ,:sql_id  )"

insert_sqlid_cluster_wait_time = "insert into sql_cluster_wait_time(instance_name ,dbid,\
begin_date,end_date,begin_snap_id ,end_snap_id,cluster_wait_time ,ela  ,\
total,elapsed_time ,cpu_time ,executions  ,sql_id )\
values(:instance_name ,:dbid,\
:begin_date,:end_date,:begin_snap_id ,:end_snap_id,:cluster_wait_time ,:ela  ,\
:total,:elapsed_time ,:cpu_time ,:executions  ,:sql_id )"

select_check_awrfile= 'select count(*) from LOAD_PROFILE where awr_file_name=:awr_file_name'