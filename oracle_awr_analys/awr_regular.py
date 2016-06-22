#!/usr/bin/env python
import re
import datetime
import awr_constant
import awr_configure
import awr_debug
import time
import os

def get_awrData(file_name):
     
    result_stat={}                                  #the result of "Load Profile"
    
    result_efficiency={}                            #the result of "Instance Efficiency Percentages"

    max_wait_event= awr_configure.num_wait_event    #the number of collected event   
    tmp_result_event={}                             #the temp   of "Foreground Wait Events" 
    result_event=[]                                 #the result of "Foreground Wait Events"    

    
    tmp_sqlid_elapsed_time = {}                     #the temp of "SQL ordered by Elapsed Time"
    result_sqlid_elapsed_time=[]                    #the result of "SQL ordered by Elapsed Time"
 
    tmp_sqlid_cpu_time = {}                         #the temp of "SQL ordered by CPU Time"
    result_sqlid_cpu_time=[]                        #the result of "SQL ordered by CPU Time"   
 
    tmp_sqlid_buffer_gets = {}                      #the temp of "SQL ordered by Gets"
    result_sqlid_buffer_gets=[]                     #the result of "SQL ordered by Gets"   
    
    tmp_sqlid_physical_read = {}                    #the temp of "SQL ordered by Read"
    result_sqlid_physical_read=[]                   #the result of "SQL ordered by Read"   

    tmp_sqlid_executions = {}                       #the temp of "SQL ordered by Read"
    result_sqlid_executions=[]                      #the result of "SQL ordered by Read"   

    tmp_sqlid_cluster_wait_time = {}                #the temp of "SQL ordered by Read"
    result_sqlid_cluster_wait_time=[]               #the result of "SQL ordered by Read"   

    #open awr file
    file_obj = open(file_name)
    
    #get file_name without path
#    result_stat['awr_file_name']=file_name[file_name.rfind('/')+1:]    
    
    awr_regular_log = file_name+'\n'
    
    for line in iter(file_obj):
        
        #get instance_name and db_id
        m= re.search(awr_constant.re_instance_name,line)
        if m <> None:
            line= file_obj.next()
            m= re.search(awr_constant.re_instance_result,line)
            if m <> None:
                result_stat['dbid']=m.group('dbid')
                result_stat['instance_name']=m.group('instance_name')
                
                result_efficiency['dbid']=m.group('dbid')
                result_efficiency['instance_name']=m.group('instance_name')
                
                tmp_result_event['dbid']=m.group('dbid')
                tmp_result_event['instance_name']=m.group('instance_name')

                tmp_sqlid_elapsed_time['dbid']=m.group('dbid')
                tmp_sqlid_elapsed_time['instance_name']=m.group('instance_name')

                tmp_sqlid_cpu_time['dbid']=m.group('dbid')
                tmp_sqlid_cpu_time['instance_name']=m.group('instance_name') 
                               
                tmp_sqlid_buffer_gets['dbid']=m.group('dbid')
                tmp_sqlid_buffer_gets['instance_name']=m.group('instance_name')          

                tmp_sqlid_physical_read['dbid']=m.group('dbid')
                tmp_sqlid_physical_read['instance_name']=m.group('instance_name')                

                tmp_sqlid_executions['dbid']=m.group('dbid')
                tmp_sqlid_executions['instance_name']=m.group('instance_name')                   

                tmp_sqlid_cluster_wait_time['dbid']=m.group('dbid')
                tmp_sqlid_cluster_wait_time['instance_name']=m.group('instance_name')   
                
                awr_regular_log += '[dbid:'+ m.group('dbid') +']'
        
        #get begin_snap_id and begin_data
        m= re.search(awr_constant.re_begin_snap,line)
        if m <> None:
            result_stat['begin_snap_id']=  m.group('begin_snap_id')
            result_stat['begin_date']=  datetime.datetime.strptime(m.group('begin_date'), '%d-%b-%y %H:%M:%S')
            
            result_efficiency['begin_snap_id']=m.group('begin_snap_id')
            result_efficiency['begin_date']=datetime.datetime.strptime(m.group('begin_date'), '%d-%b-%y %H:%M:%S')
            
            tmp_result_event['begin_snap_id']=m.group('begin_snap_id')
            tmp_result_event['begin_date']=datetime.datetime.strptime(m.group('begin_date'), '%d-%b-%y %H:%M:%S')
 
            tmp_sqlid_elapsed_time['begin_snap_id']=m.group('begin_snap_id')
            tmp_sqlid_elapsed_time['begin_date']=datetime.datetime.strptime(m.group('begin_date'), '%d-%b-%y %H:%M:%S')           

            tmp_sqlid_cpu_time['begin_snap_id']=m.group('begin_snap_id')
            tmp_sqlid_cpu_time['begin_date']=datetime.datetime.strptime(m.group('begin_date'), '%d-%b-%y %H:%M:%S')                    

            tmp_sqlid_buffer_gets['begin_snap_id']=m.group('begin_snap_id')
            tmp_sqlid_buffer_gets['begin_date']=datetime.datetime.strptime(m.group('begin_date'), '%d-%b-%y %H:%M:%S')                    

            tmp_sqlid_physical_read['begin_snap_id']=m.group('begin_snap_id')
            tmp_sqlid_physical_read['begin_date']=datetime.datetime.strptime(m.group('begin_date'), '%d-%b-%y %H:%M:%S')                    

            tmp_sqlid_executions['begin_snap_id']=m.group('begin_snap_id')
            tmp_sqlid_executions['begin_date']=datetime.datetime.strptime(m.group('begin_date'), '%d-%b-%y %H:%M:%S')                    
            
            tmp_sqlid_cluster_wait_time['begin_snap_id']=m.group('begin_snap_id')
            tmp_sqlid_cluster_wait_time['begin_date']=datetime.datetime.strptime(m.group('begin_date'), '%d-%b-%y %H:%M:%S')                    
 
            awr_regular_log +=' snap_id['+ m.group('begin_snap_id')+'-'

        #get end_snap_id and end_data
        m= re.search(awr_constant.re_end_snap,line)
        if m <> None:
            result_stat['end_snap_id']=  m.group('end_snap_id')
            result_stat['end_date']=  datetime.datetime.strptime(m.group('end_date'), '%d-%b-%y %H:%M:%S')

            result_efficiency['end_snap_id']=m.group('end_snap_id')
            result_efficiency['end_date']=datetime.datetime.strptime(m.group('end_date'), '%d-%b-%y %H:%M:%S')
            
            tmp_result_event['end_snap_id']=m.group('end_snap_id')
            tmp_result_event['end_date']=datetime.datetime.strptime(m.group('end_date'), '%d-%b-%y %H:%M:%S')
 
            tmp_sqlid_elapsed_time['end_snap_id']=m.group('end_snap_id')
            tmp_sqlid_elapsed_time['end_date']=datetime.datetime.strptime(m.group('end_date'), '%d-%b-%y %H:%M:%S')  
 
            tmp_sqlid_cpu_time['end_snap_id']=m.group('end_snap_id')
            tmp_sqlid_cpu_time['end_date']=datetime.datetime.strptime(m.group('end_date'), '%d-%b-%y %H:%M:%S')             

            tmp_sqlid_buffer_gets['end_snap_id']=m.group('end_snap_id')
            tmp_sqlid_buffer_gets['end_date']=datetime.datetime.strptime(m.group('end_date'), '%d-%b-%y %H:%M:%S')             

            tmp_sqlid_physical_read['end_snap_id']=m.group('end_snap_id')
            tmp_sqlid_physical_read['end_date']=datetime.datetime.strptime(m.group('end_date'), '%d-%b-%y %H:%M:%S')             

            tmp_sqlid_executions['end_snap_id']=m.group('end_snap_id')
            tmp_sqlid_executions['end_date']=datetime.datetime.strptime(m.group('end_date'), '%d-%b-%y %H:%M:%S')             
            
            tmp_sqlid_cluster_wait_time['end_snap_id']=m.group('end_snap_id')
            tmp_sqlid_cluster_wait_time['end_date']=datetime.datetime.strptime(m.group('end_date'), '%d-%b-%y %H:%M:%S')             
            
            awr_regular_log += m.group('end_snap_id') + ']'                                                 
        #get db_time
        m= re.search(awr_constant.re_db_time,line)
        if m <> None:
#            print m.string
#            print float(m.group('db_time_s').replace(',','')) 
            result_stat['db_time_s']=  float(m.group('db_time_s').replace(',',''))
            
        #get db_cpu
        m= re.search(awr_constant.re_db_cpu,line)
        if m <> None:
#            print m.string
#            print float(m.group('db_cpu_s').replace(',','')) 
            result_stat['db_cpu_s']=  float(m.group('db_cpu_s').replace(',',''))             
 
        #get redo size
        m= re.search(awr_constant.re_redo_size,line)
        if m <> None:
#            print m.string
#            print float(m.group('redo_size_s').replace(',','')) 
            result_stat['redo_size_s']=  float(m.group('redo_size_s').replace(',',''))   

        #get logical read
        m= re.search(awr_constant.re_logical_read,line)
        if m <> None:
#            print m.string
#            print float(m.group('logical_read_s').replace(',','')) 
            result_stat['logical_read_s']=  float(m.group('logical_read_s').replace(',',''))   

        #get blocl_changes
        m= re.search(awr_constant.re_block_changes,line)
        if m <> None:
#            print m.string
#            print float(m.group('block_chagnes_s').replace(',','')) 
            result_stat['block_chagnes_s']=  float(m.group('block_chagnes_s').replace(',',''))   

        #get physical read
        m= re.search(awr_constant.re_physical_read,line)
        if m <> None:
            result_stat['physical_read_s']=  float(m.group('physical_read_s').replace(',',''))

        #get physical write
        m= re.search(awr_constant.re_physical_write,line)
        if m <> None:
#            print m.string
#            print float(m.group('physical_write_s').replace(',','')) 
            result_stat['physical_write_s']=  float(m.group('physical_write_s').replace(',',''))   

        #get user calls
        m= re.search(awr_constant.re_user_calls,line)
        if m <> None:
#            print m.string
#            print float(m.group('user_call_s').replace(',','')) 
            result_stat['user_call_s']=  float(m.group('user_call_s').replace(',','')) 
        
        #get parse
        m= re.search(awr_constant.re_parses,line)
        if m <> None:
#            print m.string
#            print float(m.group('parse_s').replace(',','')) 
            result_stat['parse_s']=  float(m.group('parse_s').replace(',',''))         

        #get hard parse
        m= re.search(awr_constant.re_hard_parses,line)
        if m <> None:
#            print m.string
#            print float(m.group('hard_parse_s').replace(',','')) 
            result_stat['hard_parse_s']=  float(m.group('hard_parse_s').replace(',',''))   
            
        #get  W/A MB processed
        m= re.search(awr_constant.re_wa_mb_processed,line)
        if m <> None:
#            print m.string
#            print float(m.group('wa_mb_processed_s').replace(',','')) 
            result_stat['wa_mb_processed_s']=  float(m.group('wa_mb_processed_s').replace(',',''))           

        #get logons
        m= re.search(awr_constant.re_logons,line)
        if m <> None:
#            print m.string
#            print float(m.group('logons_s').replace(',','')) 
            result_stat['logons_s']=  float(m.group('logons_s').replace(',',''))      

        #get executes
        m= re.search(awr_constant.re_executes,line)
        if m <> None:
#            print m.string
#            print float(m.group('executes_s').replace(',','')) 
            result_stat['executes_s']=  float(m.group('executes_s').replace(',',''))     

        #get rollback
        m= re.search(awr_constant.re_rollbacks,line)
        if m <> None:
#            print m.string
#            print float(m.group('rollbacks_s').replace(',','')) 
            result_stat['rollbacks_s']=  float(m.group('rollbacks_s').replace(',',''))     

        #get transactions
        m= re.search(awr_constant.re_trans,line)
        if m <> None:
#            print m.string
#            print float(m.group('transactions_s').replace(',','')) 
            result_stat['transactions_s']=  float(m.group('transactions_s').replace(',',''))     

        #get buffer nowait and redo nowait
        m= re.search(awr_constant.re_buffer_redo_nowait,line)
        if m <> None:
#            print m.string
#            print float(m.group('buffer_nowait').replace(',','')) 
            result_efficiency['buffer_nowait']=  float(m.group('buffer_nowait').replace(',',''))    
#            print float(m.group('redo_nowait').replace(',','')) 
            result_efficiency['redo_nowait']=  float(m.group('redo_nowait').replace(',',''))               

        #get buffer hit and in memory sort
        m= re.search(awr_constant.re_buffer_hint_InMemory_sort,line)
        if m <> None:
#            print m.string
#            print float(m.group('buffer_hit').replace(',','')) 
            result_efficiency['buffer_hit']=  float(m.group('buffer_hit').replace(',',''))    
#            print float(m.group('InMemory_sort').replace(',','')) 
            result_efficiency['InMemory_sort']=  float(m.group('InMemory_sort').replace(',',''))    

        #get library hit and soft parse
        m= re.search(awr_constant.re_library_hit_soft_parse,line)
        if m <> None:
#            print m.string
#            print float(m.group('library_hit').replace(',','')) 
            result_efficiency['library_hit']=  float(m.group('library_hit').replace(',',''))    
#            print float(m.group('soft_parse').replace(',','')) 
            result_efficiency['soft_parse']=  float(m.group('soft_parse').replace(',',''))   

        #get Execute to Parse and latch hit
        m= re.search(awr_constant.re_exec_parse_latch_hit,line)
        if m <> None:
#            print m.string
#            print float(m.group('exec_parse').replace(',','')) 
            result_efficiency['exec_parse']=  float(m.group('exec_parse').replace(',',''))    
#            print float(m.group('latch_hit').replace(',','')) 
            result_efficiency['latch_hit']=  float(m.group('latch_hit').replace(',',''))   
 
        #get parse cpu and parse elapsd
        m= re.search(awr_constant.re_parse_cpu_parse,line)
        if m <> None:
#            print m.string
#            print float(m.group('parse_cpu').replace(',','')) 
            result_efficiency['parseCPU_parseElapsd']=  float(m.group('parseCPU_parseElapsd').replace(',',''))    
#            print float(m.group('parse_elapsd').replace(',','')) 
            result_efficiency['nonParse_CPU']=  float(m.group('nonParse_CPU').replace(',',''))   

        #get cpu usage
        m= re.search(awr_constant.re_cpu_usage,line)
        if m <> None:
            awr_debug.d_print (m.string,2)
            line = file_obj.next()
                
            m= re.search(awr_constant.re_cpu_usage_value,line)
            if m <> None:
                awr_debug.d_print (m.string,2)                    
                awr_debug.d_print (float(m.group('User')),2) 
                awr_debug.d_print (float(m.group('System')),2)
                awr_debug.d_print (float(m.group('WIO')),2)
                awr_debug.d_print (float(m.group('Idle')),2)                 
                                      
                result_efficiency['user_cpu']=  float(m.group('User'))                 
                result_efficiency['sys_cpu']= float(m.group('System')) 
                result_efficiency['wio_cpu']=  float(m.group('WIO'))                      
                result_efficiency['idle_cpu']= float(m.group('Idle'))              

        #get Foreground Wait Events
        m= re.search(awr_constant.re_foreground_waitEvent,line)
        if m <> None:
#            print m.string
            j = 0
            while j < max_wait_event:
                line = file_obj.next()
                if line == '\n': #if '\n',ignore this line
                    j -=1 
                j += 1 # next line
                m= re.search(awr_constant.re_waitEvent_value,line)
                if m <> None:
#                    print m.string                     
#                    print m.group('wait_name') 
#                    print int(m.group('waits').replace(',','')) 
#                    print int(m.group('time_outs').replace(',','')) 
#                    print int(m.group('total_wait_time').replace(',',''))                     
#                    print int(m.group('avg_wait_time').replace(',','')) 
#                    print float(m.group('waits_txn').replace(',','')) 
#                    print float(m.group('wait_db_time').replace(',','')) 
                                                           
                    tmp_result_event['wait_name']=  m.group('wait_name')                  
                    tmp_result_event['waits']=  int(m.group('waits').replace(',',''))  
                    tmp_result_event['time_outs']=  int(m.group('time_outs').replace(',',''))                        
                    tmp_result_event['total_wait_time']=  int(m.group('total_wait_time').replace(',',''))                    
                    tmp_result_event['avg_wait_time']=  int(m.group('avg_wait_time').replace(',',''))                  
                    tmp_result_event['waits_txn']=  float(m.group('waits_txn').replace(',',''))                                             
                    tmp_result_event['wait_db_time']=  float(m.group('wait_db_time').replace(',',''))   
                    
                    result_event.append(tmp_result_event.copy())                                      
     
        #get SQL ordered by Elapsed Time
        m= re.search(awr_constant.re_sql_elapsed_time,line)

        if m <> None:
#            print m.string
            while True:
                line = file_obj.next()       
  
                m= re.search(awr_constant.re_sqlid_elapsed_time,line)
                if m <> None:
#                    print m.string 
#                    print int(m.group('elapsed_time').replace(',',''))
#                    print int(m.group('cpu_time').replace(',',''))
#                    print int(m.group('executions').replace(',',''))
#                    print float(m.group('elap_per_exec').replace(',',''))  
#                    print float(m.group('total_db_time').replace(',',''))  
#                    print m.group('sql_id')
                    
                    tmp_sqlid_elapsed_time['elapsed_time']=int(m.group('elapsed_time').replace(',',''))
                    tmp_sqlid_elapsed_time['cpu_time']=int(m.group('cpu_time').replace(',',''))
                    tmp_sqlid_elapsed_time['executions']=int(m.group('executions').replace(',',''))
                    tmp_sqlid_elapsed_time['elap_per_exec']=float(m.group('elap_per_exec').replace(',','')) 
                    tmp_sqlid_elapsed_time['total_db_time']=float(m.group('total_db_time').replace(',','')) 
                    tmp_sqlid_elapsed_time['sql_id']=m.group('sql_id')
                    
                    result_sqlid_elapsed_time.append(tmp_sqlid_elapsed_time.copy())
                                                                             
                m = re.search(awr_constant.re_sqlid__end,line) # stop when "Back to SQL Statistics "
                if m <> None:
                    break
         
        #get SQL ordered by CPU Time
        m= re.search(awr_constant.re_sql_cpu_time,line)

        if m <> None:
#            print m.string
            while True:
                line = file_obj.next()       
  
                m= re.search(awr_constant.re_sqlid_cpu_time,line)
                if m <> None:
#                    print m.string 
#                    print int(m.group('cpu_time').replace(',',''))
#                    print int(m.group('elapsed_time').replace(',',''))
#                    print int(m.group('executions').replace(',',''))                    
#                    print float(m.group('cpu_per_exec').replace(',',''))  
#                    print float(m.group('total').replace(',',''))  
#                    print float(m.group('total_db_time').replace(',',''))  
#                    print m.group('sql_id') 

                    tmp_sqlid_cpu_time['cpu_time']=int(m.group('cpu_time').replace(',',''))
                    tmp_sqlid_cpu_time['elapsed_time']=int(m.group('elapsed_time').replace(',',''))
                    tmp_sqlid_cpu_time['executions']=int(m.group('executions').replace(',',''))
                    tmp_sqlid_cpu_time['cpu_per_exec']=float(m.group('cpu_per_exec').replace(',',''))
                    tmp_sqlid_cpu_time['total']=float(m.group('total').replace(',',''))
                    tmp_sqlid_cpu_time['total_db_time']=float(m.group('total_db_time').replace(',','')) 
                    tmp_sqlid_cpu_time['sql_id']=m.group('sql_id')
                    
                    result_sqlid_cpu_time.append(tmp_sqlid_cpu_time.copy())

                m = re.search(awr_constant.re_sqlid__end,line) # stop when "Back to SQL Statistics "
                if m <> None:
                    break
            
        #SQL ordered by Gets
        m= re.search(awr_constant.re_sql_buffer_gets,line)

        if m <> None:
#            print m.string        
            while True:
                line = file_obj.next()       
  
                m= re.search(awr_constant.re_sqlid_buffer_gets,line)
                if m <> None:            
#                    print m.string
#                    print int(m.group('buffer_gets').replace(',',''))
#                    print int(m.group('executions').replace(',',''))  
#                    print float(m.group('gets_per_exec').replace(',',''))
#                    print float(m.group('total').replace(',',''))  
#                    print float(m.group('cpu_time').replace(',','')) 
#                    print float(m.group('elapsed_time').replace(',',''))                  
#                    print m.group('sql_id')   
                    
                    
                    tmp_sqlid_buffer_gets['buffer_gets']=int(m.group('buffer_gets').replace(',',''))
                    tmp_sqlid_buffer_gets['executions']=int(m.group('executions').replace(',',''))                    
                    tmp_sqlid_buffer_gets['gets_per_exec']=float(m.group('gets_per_exec').replace(',',''))                    
                    tmp_sqlid_buffer_gets['total']=float(m.group('total').replace(',',''))
                    tmp_sqlid_buffer_gets['cpu_time']=float(m.group('cpu_time').replace(',','')) 
                    tmp_sqlid_buffer_gets['elapsed_time']=float(m.group('elapsed_time').replace(',',''))
                    tmp_sqlid_buffer_gets['sql_id']=m.group('sql_id')                    
                    
                    result_sqlid_buffer_gets.append(tmp_sqlid_buffer_gets.copy())
                    
                m = re.search(awr_constant.re_sqlid__end,line) # stop when "Back to SQL Statistics "
                if m <> None:
                    break
            
        #SQL ordered by Reads
        m= re.search(awr_constant.re_sql_physical_read,line)

        if m <> None:
#            print m.string        
            while True:
                line = file_obj.next()       
  
                m= re.search(awr_constant.re_sqlid_physical_read,line)
                if m <> None:    
#                    print m.string
#                    print int(m.group('physical_read').replace(',',''))
#                    print int(m.group('executions').replace(',',''))  
#                    print float(m.group('reads_per_exec').replace(',',''))
#                    print float(m.group('total').replace(',',''))  
#                    print float(m.group('cpu_time').replace(',','')) 
#                    print float(m.group('elapsed_time').replace(',',''))                  
#                    print m.group('sql_id')  

                    tmp_sqlid_physical_read['physical_read']=int(m.group('physical_read').replace(',',''))
                    tmp_sqlid_physical_read['executions']=int(m.group('executions').replace(',',''))                    
                    tmp_sqlid_physical_read['reads_per_exec']=float(m.group('reads_per_exec').replace(',',''))                    
                    tmp_sqlid_physical_read['total']=float(m.group('total').replace(',',''))
                    tmp_sqlid_physical_read['cpu_time']=float(m.group('cpu_time').replace(',','')) 
                    tmp_sqlid_physical_read['elapsed_time']=float(m.group('elapsed_time').replace(',',''))
                    tmp_sqlid_physical_read['sql_id']=m.group('sql_id')   
                    
                    result_sqlid_physical_read.append(tmp_sqlid_physical_read.copy())
                                                        
                m = re.search(awr_constant.re_sqlid__end,line) # stop when "Back to SQL Statistics "
                if m <> None:
                    break
        
        #SQL ordered by Executions
        m= re.search(awr_constant.re_sql_executions,line)

        if m <> None:
#            print m.string 
            while True:
                line = file_obj.next()       
  
                m= re.search(awr_constant.re_sqlid_executions,line)
                if m <> None:            
#                    print m.string        
#                    print int(m.group('executions').replace(',',''))
#                    print int(m.group('row_processed').replace(',',''))  
#                    print float(m.group('rows_per_exec').replace(',',''))
#                    print float(m.group('cpu_per_exec').replace(',',''))  
#                    print float(m.group('elap_per_exec').replace(',',''))                
#                    print m.group('sql_id')                      

                    tmp_sqlid_executions['executions']=int(m.group('executions').replace(',',''))
                    tmp_sqlid_executions['row_processed']=int(m.group('row_processed').replace(',',''))                    
                    tmp_sqlid_executions['rows_per_exec']=float(m.group('rows_per_exec').replace(',',''))                    
                    tmp_sqlid_executions['cpu_per_exec']=float(m.group('cpu_per_exec').replace(',',''))
                    tmp_sqlid_executions['elap_per_exec']=float(m.group('elap_per_exec').replace(',','')) 
                    tmp_sqlid_executions['sql_id']=m.group('sql_id')   
                    
                    result_sqlid_executions.append(tmp_sqlid_executions.copy()) 
                    
                m = re.search(awr_constant.re_sqlid__end,line) # stop when "Back to SQL Statistics "
                if m <> None:
                    break             
                
                       
        #SQL ordered by Cluster Wait Time 
        m= re.search(awr_constant.re_sql_cluster_wait_time,line)

        if m <> None:
#            print m.string         
            while True:
                line = file_obj.next()       
  
                m= re.search(awr_constant.re_sqlid_cluster_wait_time,line)
                if m <> None:            
#                    print m.string      
#                    print float(m.group('cluster_wait_time').replace(',',''))
#                    print float(m.group('ela').replace(',',''))
#                    print float(m.group('total').replace(',',''))
#                    print float(m.group('elapsed_time').replace(',',''))  
#                    print float(m.group('cpu_time').replace(',',''))  
#                    print int(m.group('executions').replace(',',''))                        
#                    print m.group('sql_id')    
                    
                    tmp_sqlid_cluster_wait_time['cluster_wait_time']=float(m.group('cluster_wait_time').replace(',',''))   
                    tmp_sqlid_cluster_wait_time['ela']=float(m.group('ela').replace(',',''))   
                    tmp_sqlid_cluster_wait_time['total']=float(m.group('total').replace(',',''))   
                    tmp_sqlid_cluster_wait_time['elapsed_time']=float(m.group('elapsed_time').replace(',',''))   
                    tmp_sqlid_cluster_wait_time['cpu_time']=float(m.group('cpu_time').replace(',',''))   
                    tmp_sqlid_cluster_wait_time['executions']=int(m.group('executions').replace(',',''))   
                    tmp_sqlid_cluster_wait_time['sql_id']=m.group('sql_id') 
                   
                    result_sqlid_cluster_wait_time.append(tmp_sqlid_cluster_wait_time.copy())
                    
                    
                m = re.search(awr_constant.re_sqlid__end,line) # stop when "Back to SQL Statistics "
                if m <> None:
                    break      
                     
        #SQL ordered by Parse Calls       
        #SQL ordered by Sharable Memory        
        #SQL ordered by Version Count
        
    #print log
    awr_regular_log +=' Fetch AWR_data finished! at '\
           + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
     
    print awr_regular_log 
#    print 'echo "' + awr_regular_log+'" >>' +awr_configure.awr_log
    os.system('echo "' + awr_regular_log+'" >>' +awr_configure.awr_log)
        
    return   result_stat,result_efficiency,result_event,result_sqlid_elapsed_time,\
             result_sqlid_cpu_time,result_sqlid_buffer_gets,result_sqlid_physical_read,\
             result_sqlid_executions,result_sqlid_cluster_wait_time

if __name__ == "__main__":
    var_result_stat,\
    var_result_efficiency,\
    var_result_event, \
    var_sqlid_elapsed_time,\
    var_sqlid_cpu_time,\
    var_sql_id_buffer_gets,\
    var_sqlid_physical_read ,\
    var_sqlid_executions,\
    var_sqlid_cluster_wait_time= get_awrData('D:\\workspace\\awr_analysed\\awr\\sp_orcl1_0000.html')
    
    awr_debug.d_print ("var_result_stat:"+str(var_result_stat),1)
    awr_debug.d_print ("var_result_efficiency:"+str(var_result_efficiency),1)
    awr_debug.d_print ("var_result_event:"+str(var_result_event),1)
    awr_debug.d_print ("var_sqlid_elapsed_time:"+str(var_sqlid_elapsed_time),1)
    awr_debug.d_print ("var_sqlid_cpu_time:"+str(var_sqlid_cpu_time),1)
    awr_debug.d_print ("var_sql_id_buffer_gets:"+str(var_sql_id_buffer_gets),1)
    awr_debug.d_print ("var_sqlid_physical_read:"+str(var_sqlid_physical_read),1)
    awr_debug.d_print ("var_sqlid_executions:"+str(var_sqlid_executions),1)
    awr_debug.d_print ("var_sqlid_cluster_wait_time:"+str(var_sqlid_cluster_wait_time),1)
    
    
    