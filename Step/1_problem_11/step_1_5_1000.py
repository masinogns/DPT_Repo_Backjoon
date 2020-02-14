'''
URL : https://www.acmicpc.net/problem/1000

문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
첫째 줄에 A+B를 출력한다.

이전 풀이
print(sum(map(int, input().split())))
'''
def run(a, b):
    sum = a+b;
    return sum;

if __name__ == '__main__':
    a, b = input().split()
    sum = run(int(a),int(b))
    print(sum)