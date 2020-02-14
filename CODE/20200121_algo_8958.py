def run(number):
    for i in range(0, number):
        sum = 0;
        score = 1;

        a = input()

        for element in a:
            if element == 'O':
                sum += score
                score += 1
            elif element == 'X':
                score = 1
        print(sum)


if __name__ == '__main__':
    run(int(input()))
