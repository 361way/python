#!/usr/bin/python 
#coding=utf-8 
import MySQLdb 


def getTerm(db,tag): 
	cursor = db.cursor() 
	query = "SELECT term_id FROM wp_terms where name=%s " 
	count = cursor.execute(query,tag) 
	rows = cursor.fetchall() 
	db.commit() 
	#db.close() 
	if count: 
		term_id = [int(rows[id][0]) for id in range(count)] 
		print term_id 
		return term_id 
	else:return None 

def addTerm(db,tag): 
	cursor = db.cursor() 
	query = "INSERT into wp_terms (name,slug,term_group) values (%s,%s,0)" 
	data = (tag,tag) 
	cursor.execute(query,data) 
	db.commit() 
	term_id = cursor.lastrowid 
	sql = "INSERT into wp_term_taxonomy (term_id,taxonomy,description) values (%s,'post_tag',%s) " 
	value = (term_id,tag)
	cursor.execute(sql,value) 
	db.commit() 
	db.close() 
	return int(term_id) 


dbconn = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='useso', port=3306, charset='utf8', init_command='set names utf8') 
tags = ['mysql','1111','aaaa','bbbb','ccccc','php','abc','python','java'] 

if __name__ == "__main__":
	tagids = [] 
	for tag in tags:
		try: 
		   dbconn.ping() 
		except:
			print 'mysql connect have been close'
		   dbconn = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='useso', port=3306, charset='utf8', init_command='set names utf8') 
		termid = getTerm(dbconn,tag) 
		
		if termid: 
			print tag, 'tag id is ',termid 
			tagids.extend(termid) 
		else: 
			termid = addTerm(dbconn,tag) 
			print 'add tag',tag,'id is ' ,termid 
			tagids.append(termid) 
	print 'All tags id is ',tagids 



dbconn = torndb.Connection('localhost:3306','blog',user='root',password='cacti')
tag = "mysql"
def getTerm(db,tag):
        query = "SELECT term_id FROM wp_terms where name=%s "
        count = db.execute_rowcount(query,tag)
        print count
        rows = db.query(query,tag)  
        print rows
        for row in rows:
            print row.values()

getTerm(dbconn,tag)

def getTerm(db,tag):
        query = "SELECT term_id FROM wp_terms where name=%s "
        rows = db.query(query,tag)
        termid = []
        for row in rows:
            termid.extend(row.values())
        return termid

test = getTerm(dbconn,tag)
