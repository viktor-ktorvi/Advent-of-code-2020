from collections import Counter

if __name__ == "__main__":
    # f = open("adapters_large.txt")
    # adapter_list = f.read()
    # f.close()
    adapter_list = input()

    adapters = [int(x) for x in adapter_list.split("\n")]
    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[-1] + 3)

    diffs = [adapters[i + 1] - adapters[i] for i in range(len(adapters) - 1)]

    occurrences = Counter(diffs)

    print("The product is %d" % (occurrences[1] * occurrences[3]))
