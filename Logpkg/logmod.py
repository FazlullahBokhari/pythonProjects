import logging

logging.basicConfig(filename='log.txt',
                    level=logging.INFO, filemode='a',
                    format='%(levelname)s at %(asctime)s in %(funcName)s in %(filename) at line %(lineno)d: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')



def loginfo(fname, type, l1, l2):
    if type == 'i':
        if l2 == None:
            logging.info('The function %s is called to process %s' % (fname, l1))
        else:
            logging.info('The function %s is called to process %s and %s' % (fname, l1, l2))
    elif type == 'c':
        logging.info('The function %s is completed' % (fname))


def logerror(fname, exc):
    logging.error('The function %s errored out without processing' % (fname))
    logging.error(exc)

