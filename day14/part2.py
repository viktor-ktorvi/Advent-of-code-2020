def get_binary_combinations(numx):
    array = list(range(0, 2 ** numx))

    combinations = []
    for a in array:
        combination = []
        for i in range(numx):
            combination.append((a & 2 ** i) >> i)
        combinations.append(combination[::-1])

    return combinations


if __name__ == '__main__':
    # f = open('init_example_part2.txt', 'r')
    # instructions_str = f.read()
    # f.close()

    instructions_str = input()

    instructions = instructions_str.split('\n')
    mask = None
    mask_low2high = None
    memory = {}
    for instruction in instructions:
        tokens = instruction.split()
        if tokens[0] == 'mask':
            mask = tokens[-1]
            mask_low2high = mask[::-1]
        else:
            start = tokens[0].find('[') + 1
            end = tokens[0].find(']')

            key = int(tokens[0][start:end])
            val = int(tokens[-1])

            assert mask is not None

            combinations = get_binary_combinations(mask.count('X'))

            for combination in combinations:
                key_to_change = key

                for i in range(len(mask_low2high)):

                    if mask_low2high[i] == '0':
                        pass
                    elif mask_low2high[i] == '1':
                        key_to_change |= 2 ** i

                    elif mask_low2high[i] == 'X':
                        xval = combination.pop()
                        if xval == 0:
                            key_to_change &= ~2 ** i
                        elif xval == 1:
                            key_to_change |= 2 ** i

                memory[key_to_change] = val

    print('The sum of values in memory is {:d}'.format(sum(memory.values())))
