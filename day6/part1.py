if __name__ == "__main__":
    group_anwsers = input()
    groups = group_anwsers.split("\n\n")

    total_cnt = 0
    for group in groups:
        group_cnt = 0
        for c in range(ord('a'), ord('z') + 1):
            if chr(c) in group:
                group_cnt += 1

        total_cnt += group_cnt

    print("The total count is %d" % total_cnt)




