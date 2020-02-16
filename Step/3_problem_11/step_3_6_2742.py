

def func_print(in_num):
    flag = False
    if in_num <= 100000:
        flag = True
        variable = [x for x in range(1, in_num+1)]
        for value in reversed(variable):
            print(value)
    else:
        print("in_num의 범위가 아닙니다.")

if __name__=='__main__':
    #func_print(3)
    func_print(int(input()))
