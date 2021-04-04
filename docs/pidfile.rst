.. container:: document

   .. container:: documentwrapper

      .. container:: bodywrapper

         .. container:: body

            .. rubric:: Source code for firstline.pidfile
               :name: source-code-for-firstline.pidfile

            .. container:: highlight

               ::


                  import os
                  import logging

                  [docs]class Pidfile:

                      def __init__(self, pidfile):

                          self.log = logging.getLogger()
                          self.pidfile = pidfile

                          self.pid = str(os.getpid()) 
                      
                          self.log.debug('Writing pid %s to pidfile %s' % (self.pid, self.pidfile))
                          
                          self.pidfilehandler = open(self.pidfile, 'w')
                          self.pidfilehandler.write(self.pid)
                          self.pidfilehandler.close()

                  [docs]    def remove(self):
                          self.log.debug('Removing pidfile %s' % self.pidfile)
                          os.remove(self.pidfile)

                  [docs]    def getpid(self):
                          return self.pid

   .. container:: sphinxsidebar

      .. container:: sphinxsidebarwrapper

         .. rubric:: `firstline <../../index.md>`__
            :name: firstline
            :class: logo

         .. rubric:: Navigation
            :name: navigation

         Contents:

         -  `firstline package <../../firstline.md>`__
         -  `firstline <../../modules.md>`__

         .. container:: relations

            .. rubric:: Related Topics
               :name: related-topics

            -  `Documentation overview <../../index.md>`__

               -  `Module code <../index.md>`__

         .. container::
            :name: searchbox

            .. rubric:: Quick search
               :name: searchlabel

            .. container:: searchformwrapper

   .. container:: clearer

.. container:: footer

   ©2021, Author. \| Powered by `Sphinx
   3.5.3 <http://sphinx-doc.org/>`__ & `Alabaster
   0.7.12 <https://github.com/bitprophet/alabaster>`__
