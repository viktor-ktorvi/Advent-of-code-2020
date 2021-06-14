from day5.part1 import replaceChar
import numpy as np

if __name__ == "__main__":
    seats = input()
    lines = seats.split()
    seats_array = np.zeros((128, 8))
    kernel = np.array([[-1, -1, -1],
                       [-1, 0, -1],
                       [-1, -1, -1]])

    my_seat = None
    break_flag = False
    for line in lines:
        row_string = line[0:7]
        column_string = line[7:]

        row_string = replaceChar(row_string, 'F', '0')
        row_string = replaceChar(row_string, 'B', '1')

        column_string = replaceChar(column_string, 'L', '0')
        column_string = replaceChar(column_string, 'R', '1')

        row = int(row_string, 2)
        column = int(column_string, 2)

        seats_array[row, column] = 1
        seat_id = row * 8 + column

    print(seats_array[5:-5, :])

    for i in range(seats_array.shape[0] - 2):
        for j in range(seats_array.shape[1] - 2):
            window = seats_array[i:i + 3, j:j + 3]
            res = window + kernel
            if np.sum(np.abs(res)) < 1e-3:
                my_seat = (i + 1, j + 1)

    print("My seat is\n", my_seat)
    print("My seat ID is %d" % (my_seat[0] * 8 + my_seat[1]))