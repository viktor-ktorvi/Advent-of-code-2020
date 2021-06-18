from day9.part1 import findInvalidNumber

if __name__ == "__main__":
    # f = open("XMAS_numbers.txt")
    # xmas_numbers = f.read()
    # f.close()

    xmas_numbers = input()

    xmas = xmas_numbers.split("\n")
    xmas = [int(x) for x in xmas]

    preamble = 25

    invalid_num = findInvalidNumber(xmas, preamble)
    print("%d is invalid" % invalid_num)

    break_all = False
    for i in range(len(xmas) - 1):
        for j in range(i+1, len(xmas)):
            if sum(xmas[i:j + 1]) == invalid_num:
                print("The result is %d" % (min(xmas[i:j + 1]) + max(xmas[i:j + 1])))
                break_all = True

        if break_all:
            break
