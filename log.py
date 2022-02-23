import logging

logging.basicConfig(filename='log.txt',
                    level=logging.INFO,filemode='a',
                    format='%(levelname)s at %(asctime)s in %(funcName)s in %(filename) at line %(lineno)d: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logging.info('This is my Log file for myownproject python code')
logging.shutdown()

