if __name__ == "__main__":
    year = 2020
    report = input()
    entries = [int(i) for i in report.split()]

    break_flg = False

    for i in range(len(entries)):
        for j in range(len(entries)):
            for k in range(len(entries)):
                if entries[i] + entries[j] + entries[k] == year:
                    print(year, " = ", entries[i], " + ", entries[j], " + ", entries[k])
                    print("Product = ", entries[i] * entries[j] * entries[k])

                    break_flg = True
                    break
            if break_flg:
                break
        if break_flg:
            break
