from day13.modular_math import solve_mod_system

'''
    Followed an anwser by lhf from the following link:
    https://math.stackexchange.com/questions/1346511/system-of-modular-equations
'''

if __name__ == '__main__':
    # f = open('example_schedule.txt', 'r')
    # schedule_str = f.read()
    # f.close()

    schedule_str = input()

    schedule = schedule_str.split('\n')
    buses = schedule[1].split(',')

    offsets = list(range(0, len(buses) + 1))

    buses_and_offsets = {}
    for i in range(len(buses)):
        if buses[i] != 'x':
            buses_and_offsets[int(buses[i])] = int(buses[i]) - offsets[i]

    x = solve_mod_system(a=list(buses_and_offsets.keys()), b=list(buses_and_offsets.values()))
    print(x)
