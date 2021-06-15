def explore(outer_key, da_rules, target):
    if da_rules[outer_key] is None:
        return False

    for key in da_rules[outer_key].keys():
        if key not in da_rules.keys():
            if key == target:
                return True
            else:
                return False

        # the key is target or it contains the tatger
        if key == target:
            return True
        # else go down the rabbit hole
        else:
            found = explore(key, da_rules, target)
            if found:
                return found


def getDaRules(rules, rule_delimiter, object_delimiter):
    da_rules = {}
    for rule in rules:
        sentance_parts = rule.split(rule_delimiter)

        subject = sentance_parts[0]
        objects = sentance_parts[1].split(object_delimiter)

        obj_dict = {}
        for obj in objects:
            obj_parts = obj.split()
            if obj_parts[0] != 'no':
                num = int(obj_parts[0])
                color = obj_parts[1] + " " + obj_parts[2]
                obj_dict[color] = num
            else:
                obj_dict = None
        da_rules[subject] = obj_dict

    return da_rules


if __name__ == "__main__":
    # f = open("rulebook.txt")
    # rulebook = f.read()
    # f.close()

    rulebook = input()

    rules = rulebook.split("\n")

    rule_delimiter = " bags contain "
    object_delimiter = ','

    da_rules = getDaRules(rules, rule_delimiter, object_delimiter)
    counter = 0

    for outer_key in da_rules.keys():
        found = explore(outer_key, da_rules, target='shiny gold')
        if found:
            counter += 1

    print("The number of colors is %d" % counter)
