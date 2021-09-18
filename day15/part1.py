if __name__ == '__main__':
    # f = open('example_numbers.txt', 'r')
    # numbers_str = f.read()
    # f.close()
    numbers_str = input()
    numbers = numbers_str.split(',')
    numbers = [int(n) for n in numbers]
    numbers_dict = {}
    N = 30000000

    for i in range(len(numbers)):
        numbers_dict[numbers[i]] = i + 1

    current_num = 0
    for i in range(len(numbers) + 1, N):
        if current_num not in numbers_dict.keys():
            numbers_dict[current_num] = i
            current_num = 0
        else:
            prev_num = current_num
            current_num = i - numbers_dict[current_num]
            numbers_dict[prev_num] = i

    print(i + 1, current_num)
