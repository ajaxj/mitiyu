# -*-coding:utf-8 -*-

#测试post wp

import time
import MySQLdb
import ConfigParser
from datetime import * 
import time



def connect():
	cf = ConfigParser.ConfigParser()
	try:
		cf.read("app.conf")
		db_host = cf.get("database","db_host")
		db_user = cf.get("database","db_user")
		db_pass = cf.get("database","db_pass")
		db_name = cf.get("database","db_name")
		conn = MySQLdb.connect(host=db_host,user=db_user,passwd=db_pass,db=db_name,charset='utf8')
		sql = "SELECT id FROM wp_posts ORDER BY ID DESC LIMIT 10"
		cur = conn.cursor()
		cur.execute(sql)
		list = cur.fetchall()
		for data in list:
			print data
		cur.close()
		conn.close()
	except Exception,e:
		print e


#测试远程插入数据库
def insertTest():
	cf = ConfigParser.ConfigParser()
	try:
		cf.read("app.conf")
		db_host = cf.get("database","db_host")
		db_user = cf.get("database","db_user")
		db_pass = cf.get("database","db_pass")
		db_name = cf.get("database","db_name")
		conn = MySQLdb.connect(host=db_host,user=db_user,passwd=db_pass,db=db_name,charset='utf8')
		sql = "select ID FROM wp_posts ORDER BY ID DESC LIMIT 1";
		cur = conn.cursor()
		cur.execute(sql)
		_id =  cur.fetchone()[0] + 1
		_post_author = 1
		_post_date = datetime.now()
		_post_date = _post_date.strftime('%Y-%m-%d %H:%M:%S')
		_post_date_gmt = datetime.utcnow()
		_post_date_gmt = _post_date_gmt.strftime('%Y-%m-%d %H:%M:%S')
		# # print  _post_date,_post_date_gmt
		_post_content = "this test 4"
		_post_title = "test4"
		_post_excerpt = ""
		_post_status = "publish"#"draft"
		_comment_status = "open"
		_ping_status = "open"
		_to_ping = ""
		_pinged = ""
		_post_modified = _post_date
		_post_modified_gmt = _post_date_gmt
		_post_content_filtered = ""
		_post_parent = 0
		_guid = "http://www.geek521.com/?p=" + str(_id)
		_menu_order = 0
		_post_type = 'post'
		_comment_count = 0

		sql = "INSERT INTO wp_posts(id,post_author,post_date,post_date_gmt,post_content,post_title,post_excerpt,post_status,comment_status,ping_status,to_ping,pinged,post_modified,post_modified_gmt,\
			post_content_filtered,post_parent,guid,menu_order,post_type,comment_count)VALUES(%d,%d,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',%d,'%s',%d,'%s',%d)" %(_id,_post_author,_post_date,\
			_post_date_gmt,_post_content,_post_title,_post_excerpt,_post_status,_comment_status,_ping_status,_to_ping,_pinged,_post_modified,_post_modified_gmt,_post_content_filtered,_post_parent,_guid,_menu_order,_post_type,_comment_count)
		# print sql
		cur.execute(sql)
		conn.commit()

		_post_id = _id
		_meta_key = "_edit_lock"
		_meta_value = str(int(time.time())) + ":1"
		sql = "INSERT INTO wp_postmeta(post_id,meta_key,meta_value)VALUES(%d,'%s','%s')" %(_id,_meta_key,_meta_value)
		cur.execute(sql)
		conn.commit()

		_post_id = _id
		_meta_key = "_edit_last"
		_meta_value = "1"
		sql = "INSERT INTO wp_postmeta(post_id,meta_key,meta_value)VALUES(%d,'%s','%s')" %(_id,_meta_key,_meta_value)
		cur.execute(sql)
		conn.commit()

		_post_id = _id
		_meta_key = "Delicacy_difficulty"
		_meta_value = "1"
		sql = "INSERT INTO wp_postmeta(post_id,meta_key,meta_value)VALUES(%d,'%s','%s')" %(_id,_meta_key,_meta_value)
		cur.execute(sql)
		conn.commit()

		_object_id = _id
		_term_taxonomy_id= 1
		_term_order = 0
		sql = "INSERT INTO wp_term_relationships(object_id,term_taxonomy_id,term_order)VALUES(%d,%d,%d)" %(_object_id,_term_taxonomy_id,_term_order)
		cur.execute(sql)
		conn.commit()

		cur.close()
		conn.close()
	except Exception,e:
		print e




if __name__ == '__main__':
	# connect()
	insertTest()
	

