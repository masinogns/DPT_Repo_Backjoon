def func_input(input_num):
    sum = []
    for i in range(0, input_num):
        a,b = input().split()
        sum.append(int(a)+int(b))
    return sum

def func_output(sum_list):
    for index, value in enumerate(sum_list):
        print("Case #%d: %d" %(index+1, value))

testcase = int(input())
func_output(func_input(testcase))
