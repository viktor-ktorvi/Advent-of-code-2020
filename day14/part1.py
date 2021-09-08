if __name__ == '__main__':
    f = open('init_my_input.txt', 'r')
    instructions_str = f.read()
    f.close()

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

            for i in range(len(mask_low2high)):

                if mask_low2high[i] == 'X':
                    pass
                elif mask_low2high[i] == '1':
                    val |= 2 ** i
                elif mask_low2high[i] == '0':
                    val &= ~2 ** i

            memory[key] = val

    print('The sum of values in memory is {:d}'.format(sum(memory.values())))
