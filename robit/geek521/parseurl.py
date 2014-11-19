# -*- coding:utf-8 -*-
#/usr/bin/python
import os
import urllib2
import MySQLdb
import sys

import logging.config
import ConfigParser
import logging
import logging.config
from datetime import * 
import time
from BeautifulSoup import BeautifulSoup

logging.config.fileConfig("logger.conf")
logger = logging.getLogger()	#email log




def readUrlToHtml(url):
	try:
		req = urllib2.Request(url)
		res = urllib2.urlopen(req,timeout=30)
		_html = res.read()

		if _html is not None:
			soup = BeautifulSoup(_html)
			div = soup.find("div",{"class":"article-entry"})
			divs = str(div).replace("<div class=\"article-entry\" id=\"article_content\">","").split("<div class=\"bd-ad-bottom\" style=\"margin-top:30px\">")
			return divs[0]
		else:
			logger.error("BeautifulSoup parse itindex.net html is none")
			return None
	except Exception,e:
		# print e
		logger.error(e)


def pubwp():
	cf = ConfigParser.ConfigParser()
	try:
		cf.read("app.conf")
		db_host = cf.get("database","db_host")
		db_user = cf.get("database","db_user")
		db_pass = cf.get("database","db_pass")
		db_name = cf.get("database","db_name")
		conn = MySQLdb.connect(host=db_host,user=db_user,passwd=db_pass,db=db_name,charset='utf8')
		cur = conn.cursor()
		sql = "SELECT * FROM wp_tempposts WHERE status=0 limit 1"
		cur.execute(sql)
		_data = cur.fetchone()
		if _data is not None:
			_oldid = _data[0]
			_url = _data[1]
			_title = _data[2].encode("utf-8")
			_content = readUrlToHtml(_url)
			if(_content is not None):
				sql = "select ID FROM wp_posts ORDER BY ID DESC LIMIT 1";
				cur.execute(sql)
				_id =  cur.fetchone()[0] + 1
				_post_author = 1
				_post_date = datetime.now()
				_post_date = _post_date.strftime('%Y-%m-%d %H:%M:%S')
				_post_date_gmt = datetime.utcnow()
				_post_date_gmt = _post_date_gmt.strftime('%Y-%m-%d %H:%M:%S')
				# # print  _post_date,_post_date_gmt
				_post_content = _content
				_post_title = _title
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

				sql = "UPDATE wp_tempposts SET status=1 WHERE id= %d" %(_oldid)
				cur.execute(sql)
				conn.commit()


		cur.close()
		conn.close()
	except Exception,e:
		logger.error(e)


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
	pubwp()