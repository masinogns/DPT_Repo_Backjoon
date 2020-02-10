import unittest

"""
구현 부분
"""

def func_add(a, b):
    return a+b

"""
테스트 코드
"""
class TddTest(unittest.TestCase):
    def test_function(self):
        self.assertEqual(func_add(1,1),2)
        self.assertEqual(func_add(2,3),5)
        self.assertEqual(func_add(3,4),7)
        self.assertEqual(func_add(9,8),17)
        self.assertEqual(func_add(5,2),7)

if __name__=='__main__':
    unittest.main()
