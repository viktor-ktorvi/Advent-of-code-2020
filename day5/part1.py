def replaceChar(old_string, old_char, new_char):
    new_string = ""
    for i in range(len(old_string)):
        if old_string[i] == old_char:
            new_string += new_char
        else:
            new_string += old_string[i]

    return new_string


if __name__ == "__main__":
    seats = input()
    lines = seats.split()

    max_id = 0

    for line in lines:
        row_string = line[0:7]
        column_string = line[7:]

        row_string = replaceChar(row_string, 'F', '0')
        row_string = replaceChar(row_string, 'B', '1')

        column_string = replaceChar(column_string, 'L', '0')
        column_string = replaceChar(column_string, 'R', '1')

        row = int(row_string, 2)
        column = int(column_string, 2)
        seat_id = row * 8 + column
        if seat_id > max_id:
            max_id = seat_id

    print("Highest seat ID is %d" % max_id)
