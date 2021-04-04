.. container:: document

   .. container:: documentwrapper

      .. container:: bodywrapper

         .. container:: body

            .. rubric:: Source code for firstline.helpers.helpers
               :name: source-code-for-firstline.helpers.helpers

            .. container:: highlight

               ::

                  import os.path
                  import logging

                  log = logging.getLogger()

                  [docs]def getlogconfig(filename, debug=False):

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

   .. container:: sphinxsidebar

      .. container:: sphinxsidebarwrapper

         .. rubric:: `firstline <../../../index.md>`__
            :name: firstline
            :class: logo

         .. rubric:: Navigation
            :name: navigation

         Contents:

         -  `firstline package <../../../firstline.md>`__
         -  `firstline <../../../modules.md>`__

         .. container:: relations

            .. rubric:: Related Topics
               :name: related-topics

            -  `Documentation overview <../../../index.md>`__

               -  `Module code <../../index.md>`__

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
