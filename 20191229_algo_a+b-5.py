'''
URL, https://www.acmicpc.net/problem/10952
'''
def func_input():
    input_list = []
    while True:
        a, b = input().split()
        if (a == '0' and b == '0'):
            break
        input_list.append(int(a) + int(b))
    return input_list

def func_output(input_list):
    for var in input_list:
        print(var)

if __name__ == '__main__':
    func_output(func_input())