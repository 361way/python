1、create database and tables

#建库
CREATE DATABASE `web12306`  DEFAULT CHARACTER SET utf8;

#建表
web12306 | CREATE TABLE `web12306` (
  `user_email` varchar(100) NOT NULL DEFAULT '',
  `user_pass` varchar(100) NOT NULL DEFAULT '',
  `user_name` varchar(100) NOT NULL DEFAULT '',
  `user_id` varchar(100) NOT NULL DEFAULT '',
  `user_nic` varchar(100) NOT NULL DEFAULT '',
  `user_phone` varchar(100) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#测试sql data
mysql> insert into web12306 values
('test@361way.com','test','运维之路','410221','www.361way.com','13800000000');


2、run the code 
python main.py

3、open the browser and insert the http://ip:5000
query the information use the user_id
