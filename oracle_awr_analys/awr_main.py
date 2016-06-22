#! /usr/bin/python
import glob
import re
import awr_regular
import awr_regular2
import awr_db
import awr_configure
import os
import sys
import traceback
import awr_backup

def check_awr_version(file_name):
    #open awr file
    re_verion_result = re.compile(r'''\d +\.+ \d + \. + \d + \. + \d + \. + \d''',re.VERBOSE) 
    file_obj = open(file_name)
    
    awr_ver=''
    for line in file_obj:
        m = re.search(re_verion_result,line)
        if m <> None:
#            print "awr verion: "+m.group(0)
            awr_ver=m.group(0)
            break 
    
    file_obj.close()
    if awr_ver:
        return m.group(0)
    else :
        return "false"
    
if __name__ == "__main__":
    awr_dir_file=[] 

    for dirpath,dirnames,filenames in os.walk(awr_configure.awr_file): 
#    print dirpath
        if dirpath.endswith('/'):
            awr_dir_file.extend(glob.glob(dirpath+'*.html')) 
        else:
            awr_dir_file.extend(glob.glob(dirpath+'/'+'*.html'))
        
#print awr_dir_file 

    for var_awr_filename in awr_dir_file :
        awr_filename = var_awr_filename[var_awr_filename.rfind('/')+1:]
        print awr_filename
        awr_version=check_awr_version(var_awr_filename)
        if awr_version == "false":
            continue
        else :
            var_awr_ver=awr_version.split('.')
    #       print var_awr_ver
            try :
                if int(var_awr_ver[0]) == 11 and int(var_awr_ver[1]) == 2:
        #            print '11.2'
                    awr_stat_value,\
                         awr_efficiency_value,\
                         awr_event_value,\
                         awr_sqlid_elapsed_time,\
                         awr_sqlid_cpu_time,\
                         awr_sql_id_buffer_gets,\
                         awr_sqlid_physical_read ,\
                         awr_sqlid_executions,\
                         awr_sqlid_cluster_wait_time  = awr_regular2.get_awrData(var_awr_filename)
                else :
                    awr_stat_value,\
                         awr_efficiency_value,\
                         awr_event_value,\
                         awr_sqlid_elapsed_time,\
                         awr_sqlid_cpu_time,\
                         awr_sql_id_buffer_gets,\
                         awr_sqlid_physical_read ,\
                         awr_sqlid_executions,\
                         awr_sqlid_cluster_wait_time  = awr_regular.get_awrData(var_awr_filename)
                     
            
                #print 'awr_stat_value:'+str(awr_stat_value)
                #print 'awr_efficiency_value:'+str(awr_efficiency_value)
                #print 'awr_event_value:'+str(awr_event_value)
                #print 'awr_sqlid_elapsed_time:'+str(awr_sqlid_elapsed_time)
                #print 'awr_sqlid_cpu_time:'+str(awr_sqlid_cpu_time)
                #print 'awr_sql_id_buffer_gets:'+str(awr_sql_id_buffer_gets)
                #print 'awr_sqlid_physical_read:'+str(awr_sqlid_physical_read)
                #print 'awr_sqlid_executions:'+str(awr_sqlid_executions)
                #print 'awr_sqlid_cluster_wait_time:'+str(awr_sqlid_cluster_wait_time)
                
                #insert date to db
                awr_db.write_awrData(var_awr_filename,awr_stat_value,\
                                     awr_efficiency_value,\
                                     awr_event_value,\
                                     awr_sqlid_elapsed_time,\
                                     awr_sqlid_cpu_time,\
                                     awr_sql_id_buffer_gets,\
                                     awr_sqlid_physical_read ,\
                                     awr_sqlid_executions,\
                                     awr_sqlid_cluster_wait_time )
                #move porcessed awr_file to backup_directory
                awr_backup.awrdir_clearup()
                
            except Exception,e: 
                print e
                type, value, tb = sys.exc_info()
                os.system('echo "' + traceback.format_exception(type, value, tb)[2] +'" >>' +awr_configure.awr_log) 
                print traceback.format_exception(type, value, tb)[2]    
                continue
    
    print "process end"