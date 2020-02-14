'''
https://www.acmicpc.net/problem/1001

문제
두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
첫째 줄에 A-B를 출력한다.
'''
def run(a, b):
    if (type(a) is str and type(b) is str):
        a = int(a)
        b = int(b)
    sum = a-b
    return sum

if __name__ == '__main__':
    a, b = input().split()
    minus = run(int(a), int(b))
    print(minus)