'''
https://www.acmicpc.net/problem/10817
'''

def func_input():
    numbers=[]
    a,b,c = input().split()
    numbers.append(int(a))
    numbers.append(int(b))
    numbers.append(int(c))
    return numbers

def func_output(numbers):
    numbers.sort()
    return numbers[1]

if __name__ == "__main__":
    print(func_output(numbers = func_input()))
