import re

re_instance_name = re.compile(r'''\S
                     + DB
                     + \s
                     + Name
                     ''',re.VERBOSE)

re_instance_result = re.compile(r'''\D
                     + (?P<dbid>\d+)
                     + \S
                     + \s
                     + class='awrnc'>
                     + (?P<instance_name>\w*)
                     ''',re.VERBOSE)   
 
re_begin_snap = re.compile(r'''\S
                     + Begin
                     + \s
                     + Snap:
                     + \D
                     + (?P<begin_snap_id>\d+)
                     + \D
                     + (?P<begin_date>\S+\s\d+:\d+:\d+)
                     ''',re.VERBOSE)
 
re_end_snap = re.compile(r'''\S
                     + End
                     + \s
                     + Snap:
                     + \D
                     + (?P<end_snap_id>\d+)
                     + \D
                     + (?P<end_date>\S+\s\d+:\d+:\d+)
                     ''',re.VERBOSE)
 
re_db_time = re.compile('''DB
                     + \s #whitespace
                     + Time\(s\)
                     + \D
                     + (?P<db_time_s>\d*[,]?\d*[,]?\d+.\d+)
                         ''',re.VERBOSE)
 
re_db_cpu = re.compile('''DB
                     + \s #whitespace
                     + CPU\(s\)
                     + \D
                     + (?P<db_cpu_s>\d*[,]?\d*[,]?\d+.\d+)
                         ''',re.VERBOSE)

re_redo_size = re.compile('''Redo
                     + \s #whitespace
                     + size
                     + \D
                     + (?P<redo_size_s>\d*[,]?\d*[,]?\d+.\d+)
                         ''',re.VERBOSE)

re_logical_read = re.compile('''Logical
                     + \s #whitespace
                     + read
                     + \D
                     + (?P<logical_read_s>\d*[,]?\d*[,]?\d+.\d+)
                         ''',re.VERBOSE)

re_block_changes = re.compile('''Block
                     + \s #whitespace
                     + changes
                     + \D
                     + (?P<block_chagnes_s>\d*[,]?\d*[,]?\d+.\d+)
                         ''',re.VERBOSE)
 
re_physical_read = re.compile(r'''Physical 
                     + \s # whitespace
                     + reads #reads
                     + \D
                     + (?P<physical_read_s>\d*[,]?\d*[,]?\d+.\d+)
                     + \S
                     ''' ,re.VERBOSE)

re_physical_write = re.compile(r'''Physical 
                     + \s # whitespace
                     + writes #reads
                     + \D
                     + (?P<physical_write_s>\d*[,]?\d*[,]?\d+.\d+)
                     + \S
                     ''' ,re.VERBOSE)

re_user_calls = re.compile(r'''User 
                     + \s # whitespace
                     + calls #reads
                     + \D
                     + (?P<user_call_s>\d*[,]?\d*[,]?\d+.\d+)
                     + \S
                     ''' ,re.VERBOSE)

re_parses = re.compile(r'''Parses\:
                     + \D
                     + (?P<parse_s>\d*[,]?\d*[,]?\d+.\d+)
                     ''' ,re.VERBOSE)

re_hard_parses = re.compile(r'''Hard
                     + \s
                     + parses
                     + \D
                     + (?P<hard_parse_s>\d*[,]?\d*[,]?\d+.\d+)
                     ''' ,re.VERBOSE)

re_wa_mb_processed = re.compile(r'''W/A
                     + \s
                     + MB
                     + \s
                     + processed
                     + \D
                     + (?P<wa_mb_processed_s>\d*[,]?\d*[,]?\d+.\d+)
                     ''' ,re.VERBOSE)

re_logons = re.compile(r'''Logons\:
                     + \D
                     + (?P<logons_s>\d*[,]?\d*[,]?\d+.\d+)
                     ''' ,re.VERBOSE) 

re_executes = re.compile(r'''Executes\:
                     + \D
                     + (?P<executes_s>\d*[,]?\d*[,]?\d+.\d+)
                     ''' ,re.VERBOSE) 

re_rollbacks = re.compile(r'''Rollbacks\:
                     + \D
                     + (?P<rollbacks_s>\d*[,]?\d*[,]?\d+.\d+)
                     ''' ,re.VERBOSE) 

re_trans = re.compile(r'''Transactions\:
                     + \D
                     + (?P<transactions_s>\d*[,]?\d*[,]?\d+.\d+)
                     ''' ,re.VERBOSE) 
 
re_buffer_redo_nowait = re.compile(r'''Buffer
                     + \s
                     + Nowait
                     + \D
                     + (?P<buffer_nowait>\d*[,]?\d*[,]?\d+.\d+)
                     + \D
                     + (?P<redo_nowait>\d*[,]?\d*[,]?\d+.\d+)
                     ''' ,re.VERBOSE) 
 
re_buffer_hint_InMemory_sort = re.compile(r'''Buffer
                     + \s
                     + Hit
                     + \D
                     + (?P<buffer_hit>\d*[,]?\d*[,]?\d+.\d+)
                     + \D
                     + (?P<InMemory_sort>\d*[,]?\d*[,]?\d+.\d+)
                     ''' ,re.VERBOSE)     

re_library_hit_soft_parse = re.compile(r'''Library
                     + \s
                     + Hit
                     + \D
                     + (?P<library_hit>\d*[,]?\d*[,]?\d+.\d+)
                     + \D
                     + (?P<soft_parse>\d*[,]?\d*[,]?\d+.\d+)
                     ''' ,re.VERBOSE)     

re_exec_parse_latch_hit = re.compile(r'''Execute
                     + \s
                     + to
                     + \D
                     + (?P<exec_parse>\d*[,]?\d*[,]?\d+.\d+)
                     + \D
                     + (?P<latch_hit>\d*[,]?\d*[,]?\d+.\d+)
                     ''' ,re.VERBOSE)       

re_parse_cpu_parse = re.compile(r'''Parse
                     + \s
                     + CPU
                     + \D
                     + (?P<parseCPU_parseElapsd>\d*[,]?\d*[,]?\d+.\d+)
                     + \D
                     + (?P<nonParse_CPU>\d*[,]?\d*[,]?\d+.\d+)
                     ''' ,re.VERBOSE)      
#This table displays system load statistics
re_cpu_usage = re.compile(r'''Load + \s + Average + \s + Begin''' ,re.VERBOSE)

re_cpu_usage_value = re.compile(r'''\D
                     + (?P<Load_Average_Begin>[0-9.]+)  
                     + \D
                     + (?P<Load_Average_End>[0-9.]+)
                     + \D
                     + (?P<User>[0-9.]+)
                     + \D
                     + (?P<System>[0-9.]+)
                     + \D
                     + (?P<WIO>[0-9.]+)
                     + \D
                     + (?P<Idle>[0-9.]+)
                     ''',re.VERBOSE)

re_foreground_waitEvent = re.compile(r'''Event
                     +\S +\s +\S +Waits #event wait
                     +\S +\s +\S+Time +\s +-outs # %Time -outs
                     +\S +\s +\S + Total+\s+Wait+\s+Time+\s+\(s\) #Total Wait Time
                     +\S +\s +\S + Avg + \s+wait +\s \(ms\) #Avg wait
                     +\S +\s +\S + Waits + \s + /txn # Waits /txn
                     +\S +\s +\S + \s+ DB  #db_time
                     ''' ,re.VERBOSE) 

re_waitEvent_value = re.compile(r'''awrn?c'>
                     + (?P<wait_name>[\*\:\w\s-]+)  
                     + \D
                     + (?P<waits>\d*[,]?\d*[,]?\d+)      
                     + \D
                     + (?P<time_outs>\d*[,]?\d*[,]?\d+)  
                     + \D
                     + (?P<total_wait_time>\d*[,]?\d*[,]?\d+)
                     + \D
                     + (?P<avg_wait_time>\d*[,]?\d*[,]?\d+)
                     + \D
                     + (?P<waits_txn>\d*[,]?\d*[,]?\d+.\d+)
                     + \D
                     + (?P<wait_db_time>\d*[,]?\d*[,]?\d+.\d+)
                     ''',re.VERBOSE)

re_sqlid__end =  re.compile(r'''Back + \s + to + \s + SQL + \s + Statistics ''',re.VERBOSE)

re_sql_elapsed_time = re.compile(r'''Elapsed + \s + Time + \s + \(s\)
                             + \S + \s + \S
                             + CPU
                              ''',re.VERBOSE)
 
re_sqlid_elapsed_time = re.compile(r'''awrn?c
                             + \D  
                             + (?P<elapsed_time>\d*[,]?\d*[,]?\d+)
                             + \D
                             + (?P<cpu_time>\d*[,]?\d*[,]?\d+)
                             + \D
                             + (?P<executions>\d*[,]?\d*[,]?\d+)
                             + \D
                             + (?P<elap_per_exec>\d*[,]?\d*[,]?\d+.\d+)
                             + \D
                             + (?P<total_db_time>\d*[,]?\d*[,]?\d+.\d+)
                             + ([^#]+)
                             + ([#]+)
                             + (?P<sql_id>\w+)
                              ''',re.VERBOSE)

re_sql_cpu_time = re.compile(r'''CPU + \s + Time + \s + \(s\)
                             + \S + \s + \S
                             + Elapsed + \s + Time + \s \(s\)
                             + \S + \s + \S
                             + Executions
                              ''',re.VERBOSE)    

re_sqlid_cpu_time = re.compile(r'''awrn?c
                             + \D  
                             + (?P<cpu_time>\d*[,]?\d*[,]?\d+)
                             + \D
                             + (?P<elapsed_time>\d*[,]?\d*[,]?\d+)
                             + \D
                             + (?P<executions>\d*[,]?\d*[,]?\d+)
                             + \D
                             + (?P<cpu_per_exec>\d*[,]?\d*[,]?\d+.\d+)
                             + \D
                             + (?P<total>\d*[,]?\d*[,]?\d+.\d+)
                             + \D
                             + (?P<total_db_time>\d*[,]?\d*[,]?\d+.\d+) 
                             + ([^#]+)
                             + ([#]+)
                             + (?P<sql_id>\w+)                              
                         ''',re.VERBOSE)
 
re_sql_buffer_gets = re.compile(r'''Buffer + \s + Gets + \s
                             + \S + \s + \S
                             + Executions
                              ''',re.VERBOSE)       

re_sqlid_buffer_gets = re.compile(r'''awrn?c
                             + \D  
                             + (?P<buffer_gets>\d*[,]?\d*[,]?\d+)
                             + \D
                             + (?P<executions>\d*[,]?\d*[,]?\d+)
                             + \D
                             + (?P<gets_per_exec>\d*[,]?\d*[,]?\d+.\d+)
                             + \D
                             + (?P<total>\d*[,]?\d*[,]?\d+.\d+)
                             + \D
                             + (?P<cpu_time>\d*[,]?\d*[,]?\d+.\d+) 
                             + \D
                             + (?P<elapsed_time>\d*[,]?\d*[,]?\d+.\d+) 
                             + ([^#]+)
                             + ([#]+)
                             + (?P<sql_id>\w+)                              
                         ''',re.VERBOSE)

re_sql_physical_read = re.compile(r'''Physical + \s + Read
                             + \S + \s + \S
                             + Executions
                              ''',re.VERBOSE)  
     
re_sqlid_physical_read = re.compile(r'''awrn?c
                             + \D  
                             + (?P<physical_read>\d*[,]?\d*[,]?\d+)
                             + \D
                             + (?P<executions>\d*[,]?\d*[,]?\d+)
                             + \D
                             + (?P<reads_per_exec>\d*[,]?\d*[,]?\d+.\d+)
                             + \D
                             + (?P<total>\d*[,]?\d*[,]?\d+.\d+)
                             + \D
                             + (?P<cpu_time>\d*[,]?\d*[,]?\d+.\d+) 
                             + \D
                             + (?P<elapsed_time>\d*[,]?\d*[,]?\d+.\d+) 
                             + ([^#]+)
                             + ([#]+)
                             + (?P<sql_id>\w+) 
                         ''',re.VERBOSE)

re_sql_executions = re.compile(r'''Executions + \s 
                             + \S + \s + \S
                             + Rows + \s + Processed
                              ''',re.VERBOSE)  
 
re_sqlid_executions = re.compile(r'''awrn?c
                             + \D  
                             + (?P<executions>\d*[,]?\d*[,]?\d+)
                             + \D
                             + (?P<row_processed>\d*[,]?\d*[,]?\d+)
                             + \D
                             + (?P<rows_per_exec>\d*[,]?\d*[,]?\d+.\d+)
                             + \D
                             + (?P<cpu_per_exec>\d*[,]?\d*[,]?\d+.\d+)
                             + \D
                             + (?P<elap_per_exec>\d*[,]?\d*[,]?\d+.\d+)
                             + ([^#]+)
                             + ([#]+)
                             + (?P<sql_id>\w+) 
                         ''',re.VERBOSE)

re_sql_cluster_wait_time = re.compile(r'''Cluster + \s + Wait+ \s + Time + \s + \(s\)
                             + \S + \s + \S
                             + Ela
                              ''',re.VERBOSE)  

re_sqlid_cluster_wait_time = re.compile(r'''awrn?c
                             + \D  
                             + (?P<cluster_wait_time>\d*[,]?\d*[,]?\d+.\d+)
                             + \D
                             + (?P<ela>\d*[,]?\d*[,]?\d+.\d+)
                             + \D
                             + (?P<total>\d*[,]?\d*[,]?\d+.\d+)
                             + \D
                             + (?P<elapsed_time>\d*[,]?\d*[,]?\d+.\d+)
                             + \D
                             + (?P<cpu_time>\d*[,]?\d*[,]?\d+.\d+)
                             + \D
                             + (?P<executions>\d*[,]?\d*[,]?\d+)
                             + ([^#]+)
                             + ([#]+)
                             + (?P<sql_id>\w+) 
                         ''',re.VERBOSE)
