def run(input_number):
    numbers = []
    result = 1

    for i in range(0, input_number):
        numbers.append(int(input()))

    for number in numbers:
        result = result * number

    print(str(result).count('0'))
    print(str(result).count('1'))
    print(str(result).count('2'))
    print(str(result).count('3'))
    print(str(result).count('4'))
    print(str(result).count('5'))
    print(str(result).count('6'))
    print(str(result).count('7'))
    print(str(result).count('8'))
    print(str(result).count('9'))

if __name__ == '__main__':
    run(3)