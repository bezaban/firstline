import unittest
import firstline 

class test_firstline(unittest.TestCase):
    
    def test_basic(self):
        self.assertEqual(5, 5)

    def test_configure_log_from_config(self):
        import logging
        from logging.config import dictConfig
        logging.config.dictConfig(firstline.helpers.getlogconfig('test.log', True))
        log = logging.getLogger() 
        
        log.info('Testing info log level')
        log.debug('Testing debug log level')

if __name__ == '__main__':
    unittest.main()
