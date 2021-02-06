
import os

class Pidfile:

    def __init__(self, pidfile):
      
        self.pidfile = pidfile

        self.pid = str(os.getpid()) 
        
        self.pidfilehandler = open(self.pidfile, 'w')
        self.pidfilehandler.write(self.pid)
        self.pidfilehandler.close()

    def remove(self):
        os.remove(self.pidfile)

    def getpid(self):
        return self.pid
