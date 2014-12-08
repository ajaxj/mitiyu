# -*- coding:utf-8 -*-
#/usr/bin/python
import urllib2
import MySQLdb
import logging
import logging.config
import ConfigParser
from BeautifulSoup import BeautifulSoup

logging.config.fileConfig("logger.conf")
logger = logging.getLogger()


if __name__ == '__main__':
	logger.info("this is info")