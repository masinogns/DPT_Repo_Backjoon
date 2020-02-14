import sys

def func_add(a, b):
    return a+b

def func_loop():
    for line in sys.stdin:
        a, b = line.split()
        print(func_add(int(a), int(b)))

if __name__=='__main__':
    func_loop()
