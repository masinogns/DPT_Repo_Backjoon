def func_input():
    return int(input())

def func_run(input_param):
    input_params = [list(int(x) for x in input().split())]
    if input_param == len(input_params[0]):
        max_value = max(input_params[0])
        resultset = 0
        for value in input_params[0]:
            resultset = resultset + (value / max_value)*100
        sum = resultset/input_param
    else:
        print("Not Same Lenght")
    return sum

def func_output(result_set):
    print(result_set)

if __name__ == '__main__':
    func_output(func_run(func_input()))
