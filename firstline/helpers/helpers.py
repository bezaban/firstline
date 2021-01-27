import logging
import os.path

def setuplog(logname, debug=False):
    """Initializes logging"""

    log = logging.getLogger()

    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')


    logfile = logname.split('.')[0]+'.log'
    if os.path.isdir('log'):
        logfile = 'log/'+logfile

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

