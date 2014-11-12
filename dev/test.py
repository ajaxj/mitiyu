# -*-coding:utf-8 -*-
import time
#import thread


# 不使用线程的方法
def worker():
	print "worker"
	time.sleep(1)
	return


if __name__=='__main__':
	for i in xrange(5):
		worker()
