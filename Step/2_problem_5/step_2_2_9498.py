import unittest

def func_score(in_score = 0):
    score = 'F'

    if in_score >= 90 and in_score <= 100:
        score = 'A'
    elif in_score >= 80 and in_score < 90:
        score = 'B'
    elif in_score >= 70 and in_score < 80:
        score = 'C'
    elif in_score >= 60 and in_score < 70:
        score = 'D'
    else:
        score = 'F'
    return score

def func_main():
    a = int(input())
    print(func_score(in_score=a))

# Test 코드
class TddTest(unittest.TestCase):
    def test_A_scroe(self):
        result = func_score(95)
        self.assertEqual(result, 'A')

    def test_B_scroe(self):
        result = func_score(85)
        self.assertEqual(result, 'B')

    def test_C_scroe(self):
        result = func_score(77)
        self.assertEqual(result, 'C')

if __name__=='__main__':
    unittest.main()
#    func_main()
