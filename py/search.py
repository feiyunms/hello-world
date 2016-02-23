#!/usr/bin/env python
# -*- coding: utf-8 -*-

'logging module test'

__author__='Aye'

import os
import sys

def search(path, keyword):
	for x in os.listdir(path): 
		if os.path.isdir(x):
			search(os.path.join(path, x), keyword)
		elif x.find(keyword) >= 0:
			print os.path.join(path, x)
			
if __name__=='__main__':
	args = sys.argv
	if len(args)==2:
		search(os.path.abspath('.'), args[1])
