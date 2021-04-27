# API Refrence https://github.com/xbimer/xbimer-docs

from XiR import logger

class Applet(object):
    def __init__(self):
        print('print message')
        logger.debug("debug message")
        logger.info("info message")
        logger.warn("warn message")
        logger.error("error message")


    def __kill__(self):
        print('__kill__')
