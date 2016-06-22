create table load_profile
(
  instance_name VARCHAR2(10),
  dbid          VARCHAR2(20),
  begin_date    DATE,
  end_date      DATE,
  begin_snap_id VARCHAR2(20),
  end_snap_id   VARCHAR2(20),
  awr_file_name VARCHAR2(50),
  db_time_s   NUMBER,
  db_cpu_s  NUMBER,
  redo_size_s  NUMBER,
  logical_read_s NUMBER,
  block_chagnes_s NUMBER,
  physical_read_s NUMBER,
  physical_write_s NUMBER,
  user_call_s NUMBER,
  parse_s NUMBER,
  hard_parse_s NUMBER,
  wa_mb_processed_s NUMBER,
  logons_s NUMBER,
  executes_s NUMBER,
  rollbacks_s NUMBER,
  transactions_s NUMBER
);

alter table load_profile add constraints load_profile_uk unique(dbid,instance_name,begin_snap_id,end_snap_id);
alter table load_profile add constraints load_profile_uk2 unique(awr_file_name);

create table inst_efficiency(
  instance_name VARCHAR2(10),
  dbid          VARCHAR2(20),
  begin_date    DATE,
  end_date      DATE,
  begin_snap_id VARCHAR2(20),
  end_snap_id   VARCHAR2(20),
  buffer_nowait NUMBER,
  redo_nowait NUMBER,
  buffer_hit NUMBER,
  InMemory_sort NUMBER,
  library_hit NUMBER,
  soft_parse NUMBER,
  exec_parse NUMBER,
  latch_hit NUMBER,
  parseCPU_parseElapsd NUMBER,
  nonParse_CPU NUMBER
);

alter table inst_efficiency add constraints inst_efficiency_uk unique(dbid,instance_name,begin_snap_id,end_snap_id);

create table wait_events(
  instance_name VARCHAR2(10),
  dbid          VARCHAR2(20),
  begin_date    DATE,
  end_date      DATE,
  begin_snap_id VARCHAR2(20),
  end_snap_id   VARCHAR2(20),
  wait_name  varchar2(50),
  waits			number,
  time_outs number,
  total_wait_time number,
  avg_wait_time number,
  waits_txn number,
  wait_db_time number
);

alter table wait_events add constraints wait_events_uk unique(dbid,instance_name,begin_snap_id,end_snap_id,wait_name);


create table sql_elapsed_time
(
  instance_name VARCHAR2(10),
  dbid          VARCHAR2(20),
  begin_date    DATE,
  end_date      DATE,
  begin_snap_id VARCHAR2(20),
  end_snap_id   VARCHAR2(20),
  elapsed_time number,
  cpu_time number,
  executions number,
  elap_per_exec number,
  total_db_time number,
  sql_id varchar2(20)
);

alter table sql_elapsed_time add constraints sql_elapsed_time_uk unique(dbid,instance_name,begin_snap_id,end_snap_id,sql_id);

create table sql_cpu_time
(
  instance_name VARCHAR2(10),
  dbid          VARCHAR2(20),
  begin_date    DATE,
  end_date      DATE,
  begin_snap_id VARCHAR2(20),
  end_snap_id   VARCHAR2(20),
  cpu_time number,
 elapsed_time  number,
 executions number,
 cpu_per_exec number,
 total number,
 total_db_time number,
 sql_id varchar2(20)
);

alter table sql_cpu_time add constraints sql_cpu_time_uk unique(dbid,instance_name,begin_snap_id,end_snap_id,sql_id);

create table sql_buffer_gets
(
  instance_name VARCHAR2(10),
  dbid          VARCHAR2(20),
  begin_date    DATE,
  end_date      DATE,
  begin_snap_id VARCHAR2(20),
  end_snap_id   VARCHAR2(20),
  buffer_gets number,
  executions number,
  gets_per_exec number,
  total number,
  cpu_time number,
  elapsed_time number,
 sql_id varchar2(20)  
 );
 
alter table sql_buffer_gets add constraints sql_buffer_gets_uk unique(dbid,instance_name,begin_snap_id,end_snap_id,sql_id);
 
create table sql_physical_read
(
  instance_name VARCHAR2(10),
  dbid          VARCHAR2(20),
  begin_date    DATE,
  end_date      DATE,
  begin_snap_id VARCHAR2(20),
  end_snap_id   VARCHAR2(20),
  physical_read  number,
  executions  number,
  reads_per_exec  number,
  total  number,
  cpu_time  number,
  elapsed_time  number,
  sql_id varchar2(20)  
 );

 
alter table sql_physical_read add constraints sql_physical_read_uk unique(dbid,instance_name,begin_snap_id,end_snap_id,sql_id);

create table sql_executions
(
  instance_name VARCHAR2(10),
  dbid          VARCHAR2(20),
  begin_date    DATE,
  end_date      DATE,
  begin_snap_id VARCHAR2(20),
  end_snap_id   VARCHAR2(20),
  executions number,
  row_processed number,
  rows_per_exec number,
  cpu_per_exec number,
  elap_per_exec number,
  sql_id varchar2(20)  
 );

alter table sql_executions add constraints sql_executions_uk unique(dbid,instance_name,begin_snap_id,end_snap_id,sql_id);

create table sql_cluster_wait_time
(
  instance_name VARCHAR2(10),
  dbid          VARCHAR2(20),
  begin_date    DATE,
  end_date      DATE,
  begin_snap_id VARCHAR2(20),
  end_snap_id   VARCHAR2(20),
  cluster_wait_time number,
  ela  number,
  total  number,
  elapsed_time  number,
  cpu_time  number,
  executions  number,
  sql_id varchar2(20)  
 );
 
alter table sql_cluster_wait_time add constraints sql_cluster_wait_time_uk unique(dbid,instance_name,begin_snap_id,end_snap_id,sql_id);
 