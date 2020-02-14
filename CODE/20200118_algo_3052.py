def run(input_number):
    numbers = []
    result = []

    for i in range(0, input_number):
        numbers.append(int(input()))

    for number in numbers:
        result.append(number%42)

    return len(list(set(result)))

if __name__ == '__main__':
    print(run(10))