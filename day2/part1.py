if __name__ == "__main__":
    database = input()
    lines = database.split("\n")

    valid_cnt = 0
    for line in lines:
        parts = line.split()

        numbers = parts[0].split("-")
        letter = parts[1][0]

        char_cnt = 0
        for c in parts[2]:
            if c == letter:
                char_cnt += 1

        if int(numbers[0]) <= char_cnt <= int(numbers[1]):
            valid_cnt += 1

    print("There are %d valid passwords" % valid_cnt)
