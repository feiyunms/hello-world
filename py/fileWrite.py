#!/usr/bin/env python
# -*- coding: utf-8 -*-

'codecs write Chineses test'
__author__='Aye'

import codecs
with codecs.open('./test.txt', 'w', 'gbk') as f:
	f.write(u'中文')
