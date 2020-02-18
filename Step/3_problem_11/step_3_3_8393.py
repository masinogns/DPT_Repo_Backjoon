import unittest

def func_sumary(in_num=0):
    flag  = False
    result = 0
    if in_num >= 1 and in_num <= 10000:
        flag = True
        variable = [x  for x in range(1, in_num+1)]
        for value in variable:
            result += value
    else:
        print("in_num의 범위가 넘어섰다.")
    return result


def func_main():
    a = int(input())
    print(func_sumary(a))

# Test 코드
class TddTest(unittest.TestCase):
    def test_summary_3(self):
        result = func_sumary(3)
        self.assertEqual(result, 6)

    def test_summary_10(self):
        result = func_sumary(10)
        self.assertEqual(result, 55)

if __name__=='__main__':
    unittest.main()
#    func_main()
