from day8.part1 import executeInstructions

if __name__ == "__main__":
    # f = open("boot_code.txt")
    # boot_code = f.read()
    # f.close()
    boot_code = input()

    instructions = boot_code.split("\n")

    to_change = []
    # find jmps and nops
    for i in range(len(instructions)):
        operation, argument = instructions[i].split()
        if operation == "jmp" or operation == "nop":
            to_change.append(i)

    acc = 0
    for num in to_change:
        modified = list(instructions)
        operation, argument = instructions[num].split()

        if operation == "jmp":
            operation = "nop"
        elif operation == "nop":
            operation = "jmp"

        modified[num] = operation + " " + argument
        final_i, acc = executeInstructions(modified)

        if final_i == len(instructions):
            break

    print("Accumulator = %d" % acc)
