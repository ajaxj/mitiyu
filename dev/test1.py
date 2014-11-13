# -*-coding:utf-8 -*-

#测试post wp

import time
import MySQLdb
import ConfigParser



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



if __name__ == '__main__':
	connect()

