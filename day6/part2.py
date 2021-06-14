if __name__ == "__main__":
    group_anwsers = input()
    groups = group_anwsers.split("\n\n")

    total_cnt = 0
    for group in groups:
        group_cnt = 0
        individuals = group.split()
        for c in range(ord('a'), ord('z') + 1):
            char_is_in = True
            for person in individuals:
                if chr(c) not in person:
                    char_is_in = False
                    break
            if char_is_in:
                group_cnt += 1

        total_cnt += group_cnt

    print("The total count is %d" % total_cnt)
