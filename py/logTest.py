#!/usr/bin/env python
# -*- coding: utf-8 -*-

'logging module test'
__author__='Aye'

import logging
logging.basicConfig(level=logging.INFO)

n = 10
logging.info('n = %d' % n)
print 10 / n
