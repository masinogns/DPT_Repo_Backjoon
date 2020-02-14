def run(numbers, standard):
    number_list = []
    result_list = []

    number_list = input().split()

    for i in number_list:
        if int(i) < standard:
            result_list.append(int(i))

    print(" ".join([str(i) for i in result_list] ))


if __name__ == '__main__':
    a, b = input().split()
    run(int(a), int(b))