def run(a):
    numbers = []
    numbers = list(map(int, input().split()))
    numbers.sort()
    return numbers[0], numbers[len(numbers)-1]

if __name__ == '__main__':
    a  = int(input())
    number_max, number_min = run(a)
    print(number_max)
    print(number_min)