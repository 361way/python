#! /usr/bin/python
import cx_Oracle as oracle
import awr_regular
import awr_regular2
import awr_configure
import time
import os
import sys
import traceback
import awr_backup
import awr_debug

def db_connect():
    try:
        db_conn = oracle.connect(awr_configure.oracle_username,awr_configure.oracle_password,\
                          awr_configure.oracle_tnsnames)
        #disable autocommit
        db_conn.autocommit=0
        
        return db_conn
    except Exception:
        type, value, tb = sys.exc_info()
        awr_conn_log =  traceback.format_exception(type, value, tb)[2]
        os.system('echo "' + awr_conn_log +'" >>' +awr_configure.awr_log)   
        print awr_conn_log 
        
def write_awrData(var_awr_filename,\
                  bind_stat_value,\
                  bind_efficiency_value,\
                  bind_event_value,\
                  bind_sqlid_elapsed_time,\
                  bind_sqlid_cpu_time,\
                  bind_sql_id_buffer_gets,\
                  bind_sqlid_physical_read ,\
                  bind_sqlid_executions,\
                  bind_sqlid_cluster_wait_time):
    
    conn = db_connect()
    awr_write_log=''
    if conn <> None :
        cur = conn.cursor()
        try:
            msg=''
            #write "load profile"
            if bind_stat_value['logical_read_s'] == None :
                msg+= "|no logical_read_s"
                bind_stat_value['logical_read_s']=0
                
            if bind_stat_value['physical_write_s'] == None :
                msg+= "|no physical_write_s"
                bind_stat_value['physical_write_s']=0
                
            if bind_stat_value['wa_mb_processed_s'] == None :
                msg+= "|no wa_mb_processed_s"
                bind_stat_value['wa_mb_processed_s']=0
                
            if bind_stat_value['db_cpu_s'] == None :
                msg+= "|no db_cpu_s"
                bind_stat_value['db_cpu_s']=0
                
            if bind_stat_value['physical_read_s'] == None :
                msg+= "|no physical_read_s"
                bind_stat_value['physical_read_s']=0     
                               
            if bind_stat_value['hard_parse_s'] == None :
                msg+= "|no hard_parse_s"
                bind_stat_value['hard_parse_s']=0
                
            if bind_stat_value['redo_size_s'] == None :
                msg+= "|no redo_size_s"
                bind_stat_value['redo_size_s']=0
                
            if bind_stat_value['block_chagnes_s'] == None :
                msg+= "|no block_chagnes_s"
                bind_stat_value['block_chagnes_s']=0
                
            if bind_stat_value['parse_s'] == None :
                msg+= "|no parse_s"
                bind_stat_value['parse_s']=0
                
            if bind_stat_value['rollbacks_s'] == None :
                msg+= "|no rollbacks_s"
                bind_stat_value['rollbacks_s']=0
                
            if bind_stat_value['db_time_s'] == None : 
                msg+= "|no db_time_s" 
                bind_stat_value['db_time_s']=0
                
            if bind_stat_value['executes_s'] == None : 
                msg+= "|no executes_s" 
                bind_stat_value['executes_s']=0
                
            if bind_stat_value['user_call_s'] == None : 
                msg+= "|no user_call_s" 
                bind_stat_value['user_call_s']=0
                
            if bind_stat_value['transactions_s'] == None : 
                msg+= "|no transactions_s" 
                bind_stat_value['transactions_s']=0
                
            if bind_stat_value['logons_s'] == None : 
                msg+= "|no logons_s" 
                bind_stat_value['logons_s']=0
            
            awr_write_log =var_awr_filename +'\n' + '[dbid:'+ bind_stat_value['dbid']+']'+\
                        ' snap_id['+ bind_stat_value['begin_snap_id'] +'-'+ bind_stat_value['begin_snap_id']\
                        + ']'                                                                                                                                                   
            cur.execute(awr_configure.insert_stat_value,bind_stat_value)

            awr_debug.d_print(msg, 2)
            awr_write_log += '|insert_stat_value' + msg
        
            #write "instance efficiency"
            msg=''
            if bind_efficiency_value['library_hit'] == None : 
                msg+="|no library_hit" 
                
            if bind_efficiency_value['InMemory_sort'] == None : 
                msg+= "|no InMemory_sort"
                
            if bind_efficiency_value['wio_cpu'] == None : 
                msg+= "|no wio_cpu"
                
            if bind_efficiency_value['buffer_nowait'] == None :
                msg+= "|no buffer_nowait"
                
            if bind_efficiency_value['exec_parse'] == None : 
                msg+= "|no exec_parse"
                
            if bind_efficiency_value['soft_parse'] == None : 
                msg+= "|no soft_parse"
                
            if bind_efficiency_value['sys_cpu'] == None : 
                msg+= "|no sys_cpu"
                
            if bind_efficiency_value['nonParse_CPU'] == None : 
                msg+= "|no nonParse_CPU"
                
            if bind_efficiency_value['idle_cpu'] == None : 
                msg+= "|no idle_cpu"
                
            if bind_efficiency_value['user_cpu'] == None : 
                msg+= "|no user_cpu"
                
            if bind_efficiency_value['latch_hit'] == None : 
                msg+= "|no latch_hit"
                
            if bind_efficiency_value['parseCPU_parseElapsd'] == None : 
                msg+= "|no parseCPU_parseElapsd"
                
            if bind_efficiency_value['buffer_hit'] == None : 
                msg+= "|no buffer_hit"
                
            if bind_efficiency_value['redo_nowait'] == None :
                msg+= "|no redo_nowait"
            
            print bind_efficiency_value                      
            cur.execute(awr_configure.insert_efficiency_value,bind_efficiency_value)
            awr_debug.d_print(msg, 2)
            awr_write_log += '|insert_efficiency_value' + msg

            #write wait evnet
            for tmp_bind_event_value in bind_event_value:
                msg=''
                if tmp_bind_event_value['waits'] == None :
                    msg+="|no waits"
                    tmp_bind_event_value['waits']=0
                    
                if tmp_bind_event_value['waits_txn'] == None :
                    msg+="|no waits_txn"
                    tmp_bind_event_value['waits_txn']=0
                    
                if tmp_bind_event_value['time_outs'] == None :
                    msg+="|no time_outs"
                    tmp_bind_event_value['time_outs']=0
                    
                if tmp_bind_event_value['wait_db_time'] == None :
                    msg+="|no wait_db_time"
                    tmp_bind_event_value['wait_db_time']=0
                    
                if tmp_bind_event_value['wait_name'] == None :
                    msg+="|no wait_name"
                    tmp_bind_event_value['wait_name']=0
                    
                if tmp_bind_event_value['avg_wait_time'] == None :
                    msg+="|no avg_wait_time"
                    tmp_bind_event_value['avg_wait_time']=0
                    
                if tmp_bind_event_value['total_wait_time'] == None :
                    msg+="|no total_wait_time"
                    tmp_bind_event_value['total_wait_time']=0
                                                                                                                                                            
                cur.execute(awr_configure.insert_waitEvent_value,tmp_bind_event_value)
            awr_debug.d_print(msg, 2)
            awr_write_log += '|insert_waitEvent_value' + msg
        
            #write sql order by elapsed_time 
            for tmp_bind_sqlid_elapsed_time in bind_sqlid_elapsed_time:
                msg=''
                if tmp_bind_sqlid_elapsed_time['total_db_time'] == None :
                    msg+="|no total_db_time"
                    tmp_bind_sqlid_elapsed_time['total_db_time']=0
                    
                if tmp_bind_sqlid_elapsed_time['sql_id'] == None :
                    msg+="|no sql_id"
                    tmp_bind_sqlid_elapsed_time['sql_id']=0
                    
                if tmp_bind_sqlid_elapsed_time['executions'] == None :
                    msg+="|no executions"
                    tmp_bind_sqlid_elapsed_time['executions']=0
                    
                if tmp_bind_sqlid_elapsed_time['elapsed_time'] == None :
                    msg+="|no elapsed_time"
                    tmp_bind_sqlid_elapsed_time['elapsed_time']=0
                    
                if tmp_bind_sqlid_elapsed_time['elap_per_exec'] == None :
                    msg+="|no elap_per_exec"
                    tmp_bind_sqlid_elapsed_time['elap_per_exec']=0
                
                cur.execute(awr_configure.insert_sqlid_elapsed_time,tmp_bind_sqlid_elapsed_time)
            awr_write_log += '|insert_sqlid_elapsed_time' + msg
        
            #write sql order by cpu time
            for tmp_bind_sqlid_cpu_time in bind_sqlid_cpu_time:
                msg=''
                if tmp_bind_sqlid_cpu_time['cpu_time'] == None :
                    msg+="|no cpu_time"
                    tmp_bind_sqlid_cpu_time['cpu_time']=0
                    
                if tmp_bind_sqlid_cpu_time['total_db_time'] == None :
                    msg+="|no total_db_time"
                    tmp_bind_sqlid_cpu_time['total_db_time']=0
                    
                if tmp_bind_sqlid_cpu_time['sql_id'] == None :
                    msg+="|no sql_id"
                    tmp_bind_sqlid_cpu_time['sql_id']=0
                    
                if tmp_bind_sqlid_cpu_time['cpu_per_exec'] == None :
                    msg+="|no cpu_per_exec"
                    tmp_bind_sqlid_cpu_time['cpu_per_exec']=0
                    
                if tmp_bind_sqlid_cpu_time['executions'] == None :
                    msg+="|no executions"  
                    tmp_bind_sqlid_cpu_time['executions']=0
                       
                if tmp_bind_sqlid_cpu_time['elapsed_time'] == None :
                    msg+="|no elapsed_time"  
                    tmp_bind_sqlid_cpu_time['elapsed_time']=0
                    
                if tmp_bind_sqlid_cpu_time['total'] == None :
                    msg+="|no total"  
                    tmp_bind_sqlid_cpu_time['total']=0
                    
                cur.execute(awr_configure.insert_sqlid_cpu_time,tmp_bind_sqlid_cpu_time)
            awr_write_log += '|insert_sqlid_cpu_time' + msg
        
            #write sql order by buffer gets
            for tmp_bind_sql_id_buffer_gets in bind_sql_id_buffer_gets:
                msg=''
                if tmp_bind_sql_id_buffer_gets['buffer_gets'] == None :
                    msg+="|no buffer_gets"
                if tmp_bind_sql_id_buffer_gets['cpu_time'] == None :
                    msg+="|no cpu_time"
                if tmp_bind_sql_id_buffer_gets['sql_id'] == None :
                    msg+="|no sql_id"
                if tmp_bind_sql_id_buffer_gets['executions'] == None :
                    msg+="|no executions"
                if tmp_bind_sql_id_buffer_gets['elapsed_time'] == None :
                    msg+="|no elapsed_time"     
                if tmp_bind_sql_id_buffer_gets['gets_per_exec'] == None :
                    msg+="|no gets_per_exec"  
                if tmp_bind_sql_id_buffer_gets['total'] == None :
                    msg+="|no total"  
                
                cur.execute(awr_configure.insert_sql_id_buffer_gets,tmp_bind_sql_id_buffer_gets)
            awr_write_log += '|insert_sql_id_buffer_gets' + msg
        
            #write sql order by physical read
            for tmp_bind_sqlid_physical_read in bind_sqlid_physical_read:
                msg=''
                if tmp_bind_sqlid_physical_read['cpu_time'] == None :
                    msg+="|no cpu_time"
                if tmp_bind_sqlid_physical_read['sql_id'] == None :
                    msg+="|no sql_id"
                if tmp_bind_sqlid_physical_read['executions'] == None :
                    msg+="|no executions"
                if tmp_bind_sqlid_physical_read['elapsed_time'] == None :
                    msg+="|no elapsed_time"
                if tmp_bind_sqlid_physical_read['physical_read'] == None :
                    msg+="|no physical_read"     
                if tmp_bind_sqlid_physical_read['total'] == None :
                    msg+="|no total"  
                if tmp_bind_sqlid_physical_read['reads_per_exec'] == None :
                    msg+="|no reads_per_exec" 
          
                cur.execute(awr_configure.insert_sqlid_physical_read,tmp_bind_sqlid_physical_read)
            awr_write_log += '|insert_sqlid_physical_read' + msg

            #write sql order by executions
            for tmp_bind_sqlid_executions in bind_sqlid_executions:
                msg=''
                if tmp_bind_sqlid_executions['sql_id'] == None :
                    msg+="|no sql_id"
                if tmp_bind_sqlid_executions['row_processed'] == None :
                    msg+="|no row_processed"
                if tmp_bind_sqlid_executions['rows_per_exec'] == None :
                    msg+="|no rows_per_exec"
                if tmp_bind_sqlid_executions['cpu_per_exec'] == None :
                    msg+="|no cpu_per_exec"
                if tmp_bind_sqlid_executions['executions'] == None :
                    msg+="|no executions"     
                if tmp_bind_sqlid_executions['elap_per_exec'] == None :
                    msg+="|no elap_per_exec"  

               
                cur.execute(awr_configure.insert_sqlid_executions,tmp_bind_sqlid_executions)
            awr_write_log += '|insert_sqlid_executions' + msg

            #write sql order by cluster wait time for rac
            for tmp_bind_sqlid_cluster_wait_time in bind_sqlid_cluster_wait_time:
                msg=''
                if tmp_bind_sqlid_cluster_wait_time['cpu_time'] == None :
                    msg+="|no cpu_time"
                if tmp_bind_sqlid_cluster_wait_time['cluster_wait_time'] == None :
                    msg+="|no cluster_wait_time"
                if tmp_bind_sqlid_cluster_wait_time['ela'] == None :
                    msg+="|no ela"
                if tmp_bind_sqlid_cluster_wait_time['sql_id'] == None :
                    msg+="|no sql_id"
                if tmp_bind_sqlid_cluster_wait_time['executions'] == None :
                    msg+="|no executions"     
                if tmp_bind_sqlid_cluster_wait_time['elapsed_time'] == None :
                    msg+="|no elapsed_time"
                if tmp_bind_sqlid_cluster_wait_time['total'] == None :
                    msg+="|no total"   
                
           
                cur.execute(awr_configure.insert_sqlid_cluster_wait_time,tmp_bind_sqlid_cluster_wait_time)
            awr_write_log += '|insert_sqlid_cluster_wait_time' + msg
        
            conn.commit()
        
            awr_write_log += ' Write AWR_data ' + 'finished! at '\
              + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

            os.system('echo "' + awr_write_log+'" >>' +awr_configure.awr_log)       
#           os.system(awr_write_log+awr_configure.awr_log)
            print awr_write_log
        
            var_begin_date = bind_stat_value['begin_date'].strftime('%Y%m%d')
            awr_backup.awrfile_backup(var_awr_filename,var_begin_date)
        
        except Exception:
            type, value, tb = sys.exc_info()
            awr_write_log +=  traceback.format_exception(type, value, tb)[2]
            os.system('echo "' + awr_write_log +'" >>' +awr_configure.awr_log)   
            print awr_write_log 
        finally:
            conn.close()

if __name__ == "__main__":
    awr_stat_value,\
    awr_efficiency_value,\
    awr_event_value,\
    awr_sqlid_elapsed_time,\
    awr_sqlid_cpu_time,\
    awr_sql_id_buffer_gets,\
    awr_sqlid_physical_read ,\
    awr_sqlid_executions,\
    awr_sqlid_cluster_wait_time = awr_regular2.get_awrData('D:\\workspace\\awr_analysed\\awr\\sp_irraca1_0001.html')
    
    awr_debug.d_print ("var_result_stat:"+str(awr_stat_value),1)
    awr_debug.d_print ("var_result_efficiency:"+str(awr_efficiency_value),1)
    awr_debug.d_print ("var_result_event:"+str(awr_event_value),1)
    awr_debug.d_print ("var_sqlid_elapsed_time:"+str(awr_sqlid_elapsed_time),1)
    awr_debug.d_print ("var_sqlid_cpu_time:"+str(awr_sqlid_cpu_time),1)
    awr_debug.d_print ("var_sql_id_buffer_gets:"+str(awr_sql_id_buffer_gets),1)
    awr_debug.d_print ("var_sqlid_physical_read:"+str(awr_sqlid_physical_read),1)
    awr_debug.d_print ("var_sqlid_executions:"+str(awr_sqlid_executions),1)
    awr_debug.d_print ("var_sqlid_cluster_wait_time:"+str(awr_sqlid_cluster_wait_time),1)
    
    write_awrData('D:\\workspace\\awr_analysed\\awr\\sp_irraca1_0001.html',
                  awr_stat_value,\
                  awr_efficiency_value,\
                  awr_event_value,\
                  awr_sqlid_elapsed_time,\
                  awr_sqlid_cpu_time,\
                  awr_sql_id_buffer_gets,\
                  awr_sqlid_physical_read ,\
                  awr_sqlid_executions,\
                  awr_sqlid_cluster_wait_time )