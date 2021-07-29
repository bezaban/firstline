import os.path
import logging

log = logging.getLogger()

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
        logging_config['handlers']['default']['level'] = 'DEBUG' 
        logging_config['loggers']['']['level'] = 'DEBUG' 

    return logging_config

