if __name__ == '__main__':
    # f = open('example_schedule.txt', 'r')
    # schedule_str = f.read()
    # f.close()
    schedule_str = input()
    schedule = schedule_str.split('\n')
    earliest_timestamp = int(schedule[0])
    buses_list = schedule[1].split(',')
    buses = [int(bus) for bus in buses_list if bus.isnumeric()]

    earliest_bus_time = None
    earliest_bus = None
    for bus in buses:
        modulus = earliest_timestamp % bus
        if modulus != 0:
            if earliest_bus_time is None:
                earliest_bus_time = earliest_timestamp + bus - modulus
                earliest_bus = bus

            elif earliest_timestamp + bus - modulus < earliest_bus_time:
                earliest_bus_time = earliest_timestamp + bus - modulus
                earliest_bus = bus


        else:
            earliest_bus = bus
            break

    print('Earliest bus is bus no. {:d} and I need to wait {:d} minutes.'.format(earliest_bus,
                                                                                 earliest_bus_time - earliest_timestamp))
    print('The product is {:d}'.format(earliest_bus * (earliest_bus_time - earliest_timestamp)))
