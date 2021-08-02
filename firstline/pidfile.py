"""Module to manage pidfiles"""
import os
import logging

class Pidfile:
    """Creates pidfile and writes pid"""

    def __init__(self, pidfile):
        self.log = logging.getLogger()
        self.pidfile = pidfile

        self.pid = str(os.getpid())
        self.log.debug('Writing pid %s to pidfile %s', self.pid, self.pidfile)

        with open(self.pidfile, 'w') as file:
            file.write(self.pid)

    def remove(self):
        """Removes pidfile"""
        self.log.debug("Removing pidfile %s", self.pidfile)
        os.remove(self.pidfile)

    def getpid(self):
        """Returns pid"""
        return self.pid
