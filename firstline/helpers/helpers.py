import logging
import os.path

def setuplog(logname, debug=False):
    """Initializes logging"""

    log = logging.getLogger()

    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')


    logfile = logname.split('.')[0]+'.log'
    if os.path.isdir('log'):
        logfile = 'log/{0}'.format(logfile)

    filehandler = logging.FileHandler(logfile)
    filehandler.setFormatter(formatter)

    log.addHandler(filehandler)
    log.setLevel(logging.INFO)

    if debug:
        
        streamhandler = logging.StreamHandler()
        streamhandler.setFormatter(formatter)
        
        streamhandler.setLevel(logging.DEBUG)

        log.addHandler(streamhandler)
        log.setLevel(logging.DEBUG)
        log.debug('Debug logging: %s', debug)

    return log

def getlogconfig():
    logging_config = {
        'version': 1,
        'formatters': {
            'standard': {
                'format': '[%(asctime)s] [%(levelname)s] %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            }
        },

        'handlers': {
            'default': { 
                'level': 'INFO',
                'formatter': 'standard',
                'class': 'logging.FileHandler',
                'file': 'test.log' 
            },
            'debug': { 
                'level': 'DEBUG',
                'formatter': 'standard',
                'class': 'logging.StreamHandler',
                'stream': 'ext://sys.stdout',  # Default is stderr
            }
        },
        'loggers': { 
            '': {  # root logger
                'handlers': ['default'],
                'level': 'WARNING',
                'propagate': False
            }
        }
    }

