def func_run(year):
    is_year = -1
    if (year%4 == 0) and (year%100 != 0 or year%400 == 0):
        is_year = 1
    else:
        is_year = 0
    return is_year

if __name__ == '__main__':
    input_int = int(input())
    print(func_run(input_int))