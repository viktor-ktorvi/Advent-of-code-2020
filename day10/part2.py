def explore_graph(ways_to_get_there, j):
    suma = 0
    for k in range(ways_to_get_there[j]):
        assert j - k - 1 >= 0
        if ways_to_get_there[j - k - 1] == 1:
            suma += 1
        else:
            suma += explore_graph(ways_to_get_there, j - k - 1)

    return suma


if __name__ == "__main__":
    f = open('adapters_my_input.txt')
    adapter_list = f.read()
    f.close()

    adapters = [int(x) for x in adapter_list.split("\n")]
    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[-1] + 3)

    ways_to_get_there = [0] * len(adapters)
    ways_to_get_there[0] = 1

    for i in range(len(adapters)):
        for j in range(i + 1, len(adapters)):
            if adapters[j] - adapters[i] <= 3:
                ways_to_get_there[j] += 1

    print('{:10}{:10}'.format('adapter', 'ways to get there'))
    for i in range(len(adapters)):
        print('{:10d}{:10d}'.format(adapters[i], ways_to_get_there[i]))

    distinct_ways = 1
    for i in range(len(adapters)):
        if i + 2 < len(ways_to_get_there):
            if ways_to_get_there[i] == 1 and ways_to_get_there[i + 1] == 1 and ways_to_get_there[i + 2] != 1:

                for j in range(i + 2, len(ways_to_get_there)):
                    assert j + 1 < len(ways_to_get_there)
                    if ways_to_get_there[j + 1] == 1:
                        break

                # do stuff
                # print(adapters[i], adapters[j])

                # print(explore_graph(ways_to_get_there, j))

                distinct_ways *= explore_graph(ways_to_get_there, j)

    print('Total number of distinct ways is {:d}'.format(distinct_ways))
