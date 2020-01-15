def run():
    numbers = []
    compare_num = 0

    for i in range(0, 9):
        num = int(input())
        numbers.append(num)
        if num > compare_num:
            compare_num = num
    return compare_num, numbers.index(compare_num)+1


if __name__ == '__main__':
    number_max, number_min = run()
    print(number_max)
    print(number_min)