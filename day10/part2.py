from collections import Counter


def findArrangementsRecursive(adapters, previous, all_arrangements):
    previous.append(adapters[0])
    if len(adapters) == 1:
        all_arrangements.append(previous)
        return
    for j in range(1, len(adapters)):
        if abs(adapters[j] - adapters[0]) <= 3:
            findArrangementsRecursive(adapters[j:], list(previous), all_arrangements)


def findPossibilities(adapters, i):
    possibilities = []
    for j in range(1, len(adapters) - i):
        if abs(adapters[i] - adapters[i + j]) <= 3:
            possibilities.append(j)

    return possibilities


if __name__ == "__main__":
    f = open("adapters_my_input.txt")
    adapter_list = f.read()
    f.close()
    # adapter_list = input()
    adapters = [int(x) for x in adapter_list.split("\n")]
    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[-1] + 3)

    all_arrangements = []
    # findArrangementsRecursive(adapters, [], all_arrangements)

    print(adapters)

    i = 1
    context = [adapters[0]]

    context_stack = []
    i_stack = []
    possibilities_count = [-1] * len(adapters)

    counter = 0
    while True:
        if possibilities_count[i] == 0:
            possibilities_count[i] = -1
            if not context_stack:
                break
            context = context_stack.pop()
            i = i_stack.pop()
            context.pop()
            continue


        context.append(adapters[i])
        # print(context)
        possibilities = findPossibilities(adapters, i)

        if len(possibilities) > 1:
            context_stack.append(list(context))
            i_stack.append(i)

            if possibilities_count[i] == -1:
                possibilities_count[i] = len(possibilities)

            j = i
            i += possibilities[possibilities_count[i] - 1]
            possibilities_count[j] -= 1

        else:
            i += 1

        if context[-1] == adapters[-1]:
            # print(context)
            counter += 1
            context = context_stack.pop()
            i = i_stack.pop()
            context.pop()

    print("There are %d arrangements" % counter)
