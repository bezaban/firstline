'''generic helper functions'''

import logging

def setuplog(logname, debug=False):
    """Initializes logging"""

    log = logging.getLogger(logname)

    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
    filehandler = logging.FileHandler(__package__.split('.')[0]+'.log')
    filehandler.setFormatter(formatter)

    log.addHandler(filehandler)
    log.setLevel(logging.INFO)

    if debug:
        streamhandler = logging.StreamHandler()
        streamhandler.setLevel(logging.DEBUG)
        streamhandler.setFormatter(formatter)
        log.addHandler(streamhandler)
        log.setLevel(logging.DEBUG)

    return log
