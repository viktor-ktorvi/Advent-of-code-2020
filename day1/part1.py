if __name__ == "__main__":
    year = 2020
    report = input()
    entries = [int(i) for i in report.split()]

    break_flg = False

    for i in range(len(entries)):
        for j in range(len(entries)):
            if entries[i] + entries[j] == year:
                print(year, " = ", entries[i], " + ", entries[j])
                print("Product = ", entries[i] * entries[j])

                break_flg = True
                break
        if break_flg:
            break
