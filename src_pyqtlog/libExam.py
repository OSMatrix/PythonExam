# -*- coding: utf-8 -*-

import sys
import datetime
import logging

logging.basicConfig(level=logging.INFO,
    format='%(asctime)s %(filename)s[%(lineno)3d] %(levelname)s: %(message)s') 
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def func01():
    for i in range(500):
        logger.debug('debug=>%3d' % i)
        logger.info('debug')
