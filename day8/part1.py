def executeInstructions(instructions):
    executed = set()
    i = 0
    acc = 0
    while i < len(instructions):
        if i in executed:
            break

        executed.add(i)
        operation, argument = instructions[i].split()

        if operation == "nop":
            i += 1
        elif operation == "acc":
            acc += int(argument)
            i += 1
        elif operation == "jmp":
            i += int(argument)
            if i < 0 or i >= len(instructions):
                # raise ValueError("Instruction number %d doesn't exist" % i)
                return i, acc
        else:
            raise ValueError(
                "Operation: '%s' isn't supported.\nSupported operations are 'nop', 'acc' and 'jmp'" % operation)

    return i, acc


if __name__ == "__main__":
    # f = open("boot_code.txt")
    # boot_code = f.read()
    # f.close()
    boot_code = input()

    instructions = boot_code.split("\n")

    final_i, acc = executeInstructions(instructions)
    print("Accumulator = %d" % acc)


