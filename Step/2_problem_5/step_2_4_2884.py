def func_run(hour, minute):
    target = (hour*60)+minute-45
    divide = 60
    a, b = divmod(target, divide)
    if a > 0 :
        print("{} {}".format(a, b))
    else:
        print("{} {}".format((24+a), b))

if __name__ == '__main__':
    H, M = input().split()
    func_run(int(H), int(M))
