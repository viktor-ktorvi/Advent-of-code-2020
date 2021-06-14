if __name__ == "__main__":
    database = input()
    lines = database.split("\n")

    valid_cnt = 0
    for line in lines:
        parts = line.split()

        numbers = parts[0].split("-")
        letter = parts[1][0]

        index1 = int(numbers[0]) - 1
        index2 = int(numbers[1]) - 1

        if parts[2][index1] != parts[2][index2]:
            if parts[2][index1] == letter or parts[2][index2] == letter:
                valid_cnt += 1

    print("There are %d valid passwords" % valid_cnt)