# -*- coding:utf-8 -*-

# 读取配置文件 app.conf

import ConfigParser
import logging
import logging.config



'''
#自定义logger
logger = logging.getLogger("test2")
formatter = logging.Formatter('%(name)-12s %(asctime)s %(levelname)-8s %(message)s', '%a, %d %b %Y %H:%M:%S',)
file_handler = logging.FileHandler("test.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
'''

logger = logging.getLogger()
formatter = logging.Formatter('%(name)-12s %(asctime)s %(levelname)-8s %(message)s', '%a, %d %b %Y %H:%M:%S',)
# email_handler = logging.handlers.SMTPHandler(secure=(),
#     mailhost=('smtp-mail.outlook.com', 25),
#     fromaddr='java_cn@msn.com',
#     toaddrs='java_cn@msn.com',
#     subject="your site is err logging",
#     credentials=('java_cn@msn.com', 'eeeeeeee'))

# email_handler = logging.handlers.SMTPHandler(secure=(),
#     mailhost=('smtp.163.com', 25),
#     fromaddr='tmd_sb@163.com',
#     toaddrs='tmd_sb@163.com',
#     subject="your site is err logging",
#     credentials=('tmd_sb@163.com', '273511'))
# email_handler.setFormatter(formatter)
# logger.addHandler(email_handler)




logging.config.fileConfig('logger.conf')
logger = logging.getLogger('t1')




cf = ConfigParser.ConfigParser()

try:
	cf.read("app.conf1")
	#读取配置节点
	secs = cf.sections()

	# 打印节点列表 ['database','urls']
	print 'sections',secs

	opts = cf.options("database")

	print 'options',opts

	kvs = cf.items("database")

	print 'database',kvs

	#read by type
	db_host = cf.get("database","db_host")
	print db_host

	db_pass = cf.get("database","db_pass")

	print db_pass

except Exception,e:
	logger.error(e)










