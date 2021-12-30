def find_number_next_to(line, i, direction):
    assert direction == -1 or direction == 1

    number_str = ""
    j = 1
    while line[i + direction * j] != ' ':
        number_str += line[i + direction * j]
        j += 1

        if i + direction * j > len(line) - 1:
            break

    return number_str


def in_ranges(num, ranges):
    for range_ in ranges:
        if range_[0] <= num <= range_[1]:
            return True

    return False


def get_ranges(notes):
    ranges = []

    for line in notes[:notes.find('your ticket:')].split('\n'):
        # print(line)
        for i in range(len(line)):
            if line[i] == '-':
                # isolate number to the left
                left = find_number_next_to(line, i, direction=-1)[::-1]
                # print('Left = ', left, end='\t')
                right = find_number_next_to(line, i, direction=1)
                # print('Right = ', right)

                ranges.append([int(left), int(right)])

    return ranges


if __name__ == '__main__':
    # f = open('example_notes1.txt')
    # notes = f.read()
    # f.close()

    notes = input()

    ranges = get_ranges(notes)

    error_rate = 0

    for line in notes[notes.find('nearby tickets:') + len('nearby tickets:'):].split('\n'):
        print(line)
        for number in line.split(','):
            if not number.isnumeric():
                continue

            if not in_ranges(int(number), ranges):
                print('Not in ranges ', number)
                error_rate += int(number)

    print('\nTicket scanning error rate = ', error_rate)
