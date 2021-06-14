def yearCheck(field, field_id, limits):
    if field[0:len(field_id)] == field_id:
        yr = field[len(field_id) + 1:]
        if len(yr) != 4:
            return False
        if not limits[0] <= int(yr) <= limits[1]:
            return False
        return True
    else:
        return False


if __name__ == "__main__":
    database = input()
    # f = open("input.txt", "r")
    # database = f.read()
    # f.close()
    passports = database.split("\n\n")
    fieldnames = ["byr",
                  "iyr",
                  "eyr",
                  "hgt",
                  "hcl",
                  "ecl",
                  "pid"]

    byr_limits = [1920, 2002]
    iyr_limits = [2010, 2020]
    eyr_limits = [2020, 2030]
    cm_limits = [150, 193]
    in_limits = [59, 76]
    num_hc_digits = 6

    eye_colors = ["amb",
                  "blu",
                  "brn",
                  "gry",
                  "grn",
                  "hzl",
                  "oth"]

    valid_cnt = 0
    for passport in passports:
        valid = True
        for fieldname in fieldnames:
            if passport.find(fieldname) == -1:
                valid = False
                break

        fields = passport.split()
        for field in fields:
            field_id = field[0:3]

            if field_id == "byr":
                valid = valid and yearCheck(field, "byr", byr_limits)
            if field_id == "iyr":
                valid = valid and yearCheck(field, "iyr", iyr_limits)
            if field_id == "eyr":
                valid = valid and yearCheck(field, "eyr", eyr_limits)

            if field_id == "hgt":
                height_end = field.find("cm")
                if height_end != -1:
                    height_limits = cm_limits
                else:
                    height_end = field.find("in")
                    height_limits = in_limits

                height = int(field[len("hgt") + 1:height_end])
                valid = valid and height_limits[0] <= height <= height_limits[1]

            if field_id == "hcl":
                hair_color_begin = field.find("#")
                hair_color = field[hair_color_begin:]
                hc_digits = hair_color[1:]

                valid = valid and len(hc_digits) == num_hc_digits
                for digit in hc_digits:
                    valid = valid and ('0' <= digit <= '9' or 'a' <= digit <= 'f')

            if field_id == "ecl":
                eye_color = field[len(field_id) + 1:]
                color_found = False
                for color in eye_colors:
                    color_found = color == eye_color
                    if color_found:
                        break
                valid = valid and color_found

            if field_id == "pid":
                pid = field[len(field_id) + 1:]
                valid = valid and len(pid) == 9

            if not valid:
                break

        if valid:
            valid_cnt += 1

    print("There are %d valid passports" % valid_cnt)
