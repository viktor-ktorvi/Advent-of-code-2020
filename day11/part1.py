import copy

EMPTY = 'L'
OCCUPIED = '#'


def seat_is_empty(seat):
    return seat == EMPTY


def seat_is_occupied(seat):
    return seat == OCCUPIED


def get_local_neighbourhood(i, r, limit):
    ln = list(range(-r, r + 1))
    ln = [x + i for x in ln if 0 <= x + i < limit]  # no overflow

    return ln


def count_occupied_seats(seats, row, col):
    height = len(seats)
    width = len(seats[0])

    # get local neighbourhood indices
    adjacent_i = get_local_neighbourhood(row, r=1, limit=height)
    adjacent_j = get_local_neighbourhood(col, r=1, limit=width)

    # count occupied seats in local neighbourhood
    occupied_count = 0
    for i in adjacent_i:
        for j in adjacent_j:
            if i == row and j == col:  # skip the cental seat
                continue
            else:
                if seat_is_occupied(seats[i][j]):
                    occupied_count += 1

    return occupied_count


def count_occupied_total(seats):
    occupied_count = 0

    height = len(seats)
    width = len(seats[0])

    for i in range(height):
        for j in range(width):
            if seat_is_occupied(seats[i][j]):
                occupied_count += 1

    return occupied_count


def apply_rules_to_seat(seats, seats_copy, row, col):
    occupied_count = count_occupied_seats(seats_copy, row, col)

    # check on copy, apply changes to original

    # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    if seat_is_empty(seats_copy[row][col]) and occupied_count == 0:
        seats[row][col] = OCCUPIED

    # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    if seat_is_occupied(seats_copy[row][col]) and occupied_count >= 4:
        seats[row][col] = EMPTY


def apply_rules(seats):
    height = len(seats)
    width = len(seats[0])

    seats_copy = copy.deepcopy(seats)

    # apply rules all at once, not seat by seat

    for row in range(height):
        for col in range(width):
            apply_rules_to_seat(seats, seats_copy, row, col)


if __name__ == '__main__':
    # f = open('seat_example_start.txt', 'r')
    # seats_str = f.read()
    # f.close()

    seats_str = input()

    lines = seats_str.split('\n')

    seats = []
    for line in lines:
        seats.append([char for char in line])

    previous_seats = copy.deepcopy(seats)
    apply_rules(seats)

    while previous_seats != seats:
        previous_seats = copy.deepcopy(seats)
        apply_rules(seats)

    print('Total occupied seats: ', count_occupied_total(seats))
