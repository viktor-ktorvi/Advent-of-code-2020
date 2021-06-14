if __name__ == "__main__":
    database = input()
    passports = database.split("\n\n")
    fields = ["byr",
              "iyr",
              "eyr",
              "hgt",
              "hcl",
              "ecl",
              "pid"]

    valid_cnt = 0
    for passport in passports:
        valid = True
        for field in fields:
            if passport.find(field) == -1:
                valid = False
                break

        if valid:
            valid_cnt += 1

    print("There are %d valid passports" % valid_cnt)
