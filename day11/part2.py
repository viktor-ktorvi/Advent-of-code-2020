import copy

from day11.part1 import seat_is_empty, seat_is_occupied, EMPTY, OCCUPIED, count_occupied_total


def explore_direction(seats, i, j, i_inc, j_inc):
    height = len(seats)
    width = len(seats[0])

    # walk a step in each direction

    while True:
        i += i_inc
        j += j_inc

        # if you're out of bounds then the direction is not occupied
        if not 0 <= i < height or not 0 <= j < width:
            return False

        # same if it's empty
        if seat_is_empty(seats[i][j]):
            return False

        # if it's occupied then it's occupied... duh...
        if seat_is_occupied(seats[i][j]):
            return True


def count_occupied_seats(seats, row, col):
    # get all possible directions
    i_dirs = list(range(-1, 2))
    j_dirs = list(range(-1, 2))

    occupied_count = 0

    # check if they're occupied
    for i_dir in i_dirs:
        for j_dir in j_dirs:
            if i_dir == 0 and j_dir == 0:
                continue
            else:
                if explore_direction(seats, row, col, i_dir, j_dir):
                    occupied_count += 1

    return occupied_count


def apply_rules_to_seat(seats, seats_copy, row, col):
    occupied_count = count_occupied_seats(seats_copy, row, col)

    # check on copy, apply changes to original

    # If a seat is empty (L) and there are no occupied seats in all direction, the seat becomes occupied.
    if seat_is_empty(seats_copy[row][col]) and occupied_count == 0:
        seats[row][col] = OCCUPIED

    # If a seat is occupied (#) and five or more seats in the directions around it are also occupied,
    # the seat becomes empty.
    if seat_is_occupied(seats_copy[row][col]) and occupied_count >= 5:
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
