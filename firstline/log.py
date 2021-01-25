'''generic helper functions'''

import logging

def initlog(debug=False):
    """Initializes logging"""

    log = logging.getLogger(__package__)

    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
    filehandler = logging.FileHandler(__package__.split('.')[0]+'.log')
    filehandler.setFormatter(formatter)
    log.addHandler(filehandler)
    log.setLevel(logging.INFO)

    return log

def enabledebuglog():
    """Enables debug and stdout streamhandler"""
 
    log = logging.getLogger(__package__)
    #formatter = logging.Formatter('[%(asctime)s:%(name)s][%(levelname)s] %(message)s')
    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')

    streamhandler = logging.StreamHandler()
    streamhandler.setLevel(logging.DEBUG)
    streamhandler.setFormatter(formatter)

    log.addHandler(streamhandler)
    log.setLevel(logging.DEBUG)
