def func_run(input_param_int):
    for i in range(1,10):
        print("{} * {} = {}".format(input_param_int, i, i*input_param_int))

if __name__ == '__main__':
    number = int(input())
    func_run(number)