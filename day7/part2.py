from day7.part1 import getDaRules


def exploreAndCount(outer_key, da_rules):
    if da_rules[outer_key] is None:
        return 0

    da_sum = 0
    for key in da_rules[outer_key].keys():
        da_sum += da_rules[outer_key][key] * (1 + exploreAndCount(key, da_rules))
    return da_sum


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
    target = 'shiny gold'
    counter = exploreAndCount(target, da_rules)
    print("There are %d bags inside the %s bag" % (counter, target))
