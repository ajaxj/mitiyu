# -*- coding:utf-8 -*-
import urllib2
import MySQLdb
import logging
import logging.config
import ConfigParser
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
			div_list = soup.findAll("div",{"class":"post"})
			if len(div_list) == 0:
				logger.error("BeautifulSoup parse html is none")
			else:
				for div in div_list:
					a = div.find("h2").find("a")
					_title = a.string
					_url = a.get("href")
					insertTable(_title,_url)
		else:
			logger.error("BeautifulSoup parse itindex.net html is none")
	except Exception,e:
		logger.error(e)


def insertTable(title,url):
	cf = ConfigParser.ConfigParser()
	try:
		cf.read("app.conf")
		db_host = cf.get("database","db_host")
		db_user = cf.get("database","db_user")
		db_pass = cf.get("database","db_pass")
		db_name = cf.get("database","db_name")
		conn = MySQLdb.connect(host=db_host,user=db_user,passwd=db_pass,db=db_name,charset='utf8')
		cur = conn.cursor()
		_url = url
		_title = title
		sql = "SELECT ID FROM wp_tempposts WHERE post_url = '%s' AND post_title = '%s' limit 1" %(_url,_title)
		cur.execute(sql)
		if cur.fetchone() is None:
			sql = "INSERT INTO wp_tempposts(post_url,post_title,status)VALUES('%s','%s',%d)" %(_url,_title,0)
			cur.execute(sql)
			conn.commit()
		cur.close()
		conn.close()
	except Exception,e:
		logger.error(e)



if __name__ == '__main__':
	url = "http://itindex.net"
	readUrlToHtml(url)