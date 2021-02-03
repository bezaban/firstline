import unittest
import firstline 

class testFl(unittest.TestCase):
    
    def test_basic(self):
        self.assertEqual(5, 5)

if __name__ == '__main__':
    unittest.main()
