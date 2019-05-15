# -*- coding:utf-8 -*- 
import unittest
from utils.mylog import mylog

Log = mylog()
logger = Log.get_log().get_logger()

########################################################################
class test_calc(unittest.TestCase):
    """"""
    a = 1
    b = 2 
    def setUp(self):
        logger.debug("************* START **************")
        
    #----------------------------------------------------------------------
    def test_addyy(self):
        """"""
        logger.debug("****** test_addyy ******")
        c = self.a + self.b
        self.assertEqual(c, 3)
        
    @unittest.skip("test_misyy")
    def test_misyy(self):
        logger.debug("**** test_misyy ******")
        c = self.a - self.b
        self.assertEqual(c, -2)      
    
    def test_multyy(self):
        logger.debug("***** test_multyy *****")
        c = self.a * self.b
        self.assertEqual(c, 2)           
    
    def tearDown(self):
        logger.debug("************* END **************")
    
if __name__ == '__main__':
    #test_calc()
    unittest.main()
