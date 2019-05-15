# -*- coding:utf-8 -*- 
import unittest
import sys


########################################################################
class test_calc(unittest.TestCase):
    """"""
    a = 1
    b = 2 

    #----------------------------------------------------------------------
    def test_add(self):
        """"""
        c = self.a + self.b
        self.assertEqual(c, 3)
        
    def test_mis(self):
        c = self.a - self.b
        self.assertEqual(c, -2)      
    
    def test_mult(self):
        c = self.a * self.b
        self.assertEqual(c, 3)           
    
    
if __name__ == '__main__':
    #test_calc()
    unittest.main()
