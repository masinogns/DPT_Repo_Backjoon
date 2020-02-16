def func_input(input_num):
    for i in range(0, input_num):
        a,b = input().split()
        print("Case #{}: {} + {} = {}".format(i+1, a, b, int(a)+int(b)))

if __name__=='__main__':
    testcase = int(input())
    func_input(testcase)
