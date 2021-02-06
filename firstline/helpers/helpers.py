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

def getlogconfig(filename, debug=False):

    if os.path.isdir('log'):
        filename = 'log/{0}'.format(filename)

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
                'filename': filename,
                'mode': 'a',
            },
            'debug': { 
                'level': 'DEBUG',
                'formatter': 'standard',
                'class': 'logging.StreamHandler',
                'stream': 'ext://sys.stdout'
            }
        },
        'loggers': { 
            '': {  # root logger
                'handlers': ['default'],
                'level': 'INFO',
                'propagate': False
            }
        }
    }

    if debug:
        logging_config['loggers']['']['handlers'] = ['default', 'debug']
        logging_config['loggers']['']['level'] = 'DEBUG' 

    return logging_config

