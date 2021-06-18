def findInvalidNumber(xmas, preamble):
    for i in range(preamble, len(xmas)):
        valid = False
        for j in range(1, preamble + 1):
            number1 = xmas[i - j]
            number2 = xmas[i] - number1

            if number2 in xmas[i - preamble:i] and number1 != number2:
                valid = True

        if not valid:
            return xmas[i]

    return None


if __name__ == "__main__":
    # f = open("XMAS_numbers.txt")
    # xmas_numbers = f.read()
    # f.close()

    xmas_numbers = input()

    xmas = xmas_numbers.split("\n")
    xmas = [int(x) for x in xmas]

    preamble = 25

    # complexity sucks
    print("%d is invalid!" % findInvalidNumber(xmas, preamble))
