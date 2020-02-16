def run(testcace):
    sum = []
    for i in range(0, testcase):
        a, b = input().split()
        sum.append(int(a) + int(b))
    return sum

if __name__ == '__main__':
    testcase = int(input())
    result_of_list = run(testcace=testcase)
    for i in result_of_list:
        print(i)
