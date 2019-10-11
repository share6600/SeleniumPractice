"""
Logger Demo
"""
import logging

class LoggerDemoConsole():

    def testLog(self):
        # create logger
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)

        # create console handler and set level to info
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)
        # create formatter
        formattr = logging.Formatter('%(asctime)s -%(name)s - %(levelname)s: %(message)s')

        # add formatter to console handler
        chandler.setFormatter(formattr)

        # add console handler to logger
        logger.addHandler(chandler)


        # logging messages
        logger.debug('debug message')
        logger.info('info message')
        logger.warn('warn message')
        logger.error('error message')
        logger.critical('critical message')

demo = LoggerDemoConsole()
demo.testLog()