# -*-coding:utf-8 -*-
import time
import thread

def timer(no,interval):
	print "timer"


def test():
	timer(1,2)
	timer(1,1)

if __name__ == "__main__":
	test()