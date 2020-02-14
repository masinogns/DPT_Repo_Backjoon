import sys

def run(number):
    for i in range(0, number):
        a, b = sys.stdin.readline().split()
        print(int(a)+int(b))


if __name__ == '__main__':
    a = sys.stdin.readline()
    run(int(a))