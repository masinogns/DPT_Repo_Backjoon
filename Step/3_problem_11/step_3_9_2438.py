def func_print_star(in_num=0):
    if in_num >= 1 and in_num <= 100:
        variable = ["*"*x for x in range(1, in_num+1)]
        for value in variable:
            print(value)
    else:
        print("in_num 범위가 아닙니다.")

def func_main():
    a = int(input())
    func_print_star(a)

if __name__ == '__main__':
    func_main()
