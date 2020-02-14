def run():
    result_output = ''
    a, b = input().split()
    number_a = int(a)
    number_b = int(b)
    if number_a > number_b:
        result_output = '>'
    elif number_a < number_b:
        result_output = '<'
    else:
        result_output = '=='
    return result_output

if __name__ == '__main__':
    print(run())
