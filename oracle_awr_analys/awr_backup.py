#! /usr/bin/python
import time
import os 
import shutil
import awr_configure
import glob
import sys
import traceback

def awrdir_clearup():
    current_filenames=[]
    for dirpath,dirnames,filenames in os.walk(awr_configure.awr_file): 
        for name in dirnames:
            current_filenames.append(os.path.join(dirpath,name)+'/')

    current_filenames = sorted(current_filenames,reverse=True)
    for var_dir in  current_filenames:
        try :
#            print glob.glob(var_dir+'*')
            if glob.glob(var_dir+'*')==[]:
                os.rmdir(var_dir)
        except Exception,e: 
            print e
            type, value, tb = sys.exc_info()
            awr_awrdir_clearup =  traceback.format_exception(type, value, tb)[2]
            print awr_awrdir_clearup
            os.system('echo "' + awr_awrdir_clearup+'" >>' +awr_configure.awr_log)     
    
         


def awrfile_backup(var_awr_filename,var_awr_begin_date) :
    
    #if backup dir is defined
    if os.path.exists(awr_configure.backup_dir)<>True:
        awr_backup_dir = os.getcwd() + '/backup'
        
    else:
        awr_backup_dir = awr_configure.backup_dir
    
    if not awr_backup_dir.endswith('/'):
        awr_backup_dir = awr_backup_dir + '/'
	print awr_backup_dir

    #create backup dir
#    awr_backup_dir= awr_backup_dir+ time.strftime('%Y%m%d',time.localtime(time.time()))
    if os.path.exists(awr_backup_dir)<>True:
        os.mkdir(awr_backup_dir)
    
    awr_dir_filename = var_awr_filename[var_awr_filename.rfind('/')+1:]
    awr_back_file = awr_backup_dir + awr_dir_filename+'_'+ var_awr_begin_date
    
    awr_back_log =  'backup ' + var_awr_filename +' to ' + awr_back_file + ' finished!\n' 
    print awr_back_log

    shutil.move(var_awr_filename,awr_back_file)    
    
    os.system('echo "' + awr_back_log+'" >>' +awr_configure.awr_log)     


if __name__ == "__main__":
    awrdir_clearup()
