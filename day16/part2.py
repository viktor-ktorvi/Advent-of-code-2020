from day16.part1 import get_ranges, in_ranges
import numpy as np


def get_valid_tickets(notes, ranges):
    valid_tickets = []

    for line in notes[notes.find('nearby tickets:') + len('nearby tickets:'):].split('\n'):
        ticket_is_valid = True
        for number in line.split(','):
            if not number.isnumeric():
                ticket_is_valid = False
                continue

            if not in_ranges(int(number), ranges):
                ticket_is_valid = False

        if ticket_is_valid:
            valid_tickets.append(line)

    return valid_tickets


class Field:

    def __init__(self, name, ranges, score):
        self.name = name
        self.ranges = ranges
        self.score = score
        self.position = None

    def in_ranges(self, num):
        return in_ranges(num, self.ranges)

    def vote(self, i):
        self.score[i] += 1

    def set_position(self, pos):
        self.position = pos


if __name__ == '__main__':
    f = open('my_input.txt')
    notes = f.read()
    f.close()

    ranges = get_ranges(notes)
    valid_tickets = get_valid_tickets(notes, ranges)

    # get field names
    field_names = []
    for line in notes[:notes.find('your ticket:')].split('\n'):
        # if line is not empty
        if line:
            field_names.append(line[:line.find(':')])

    # init fields
    fields = []
    for i in range(len(field_names)):
        fields.append(Field(field_names[i], ranges[2 * i:2 * (i + 1)], score=[0] * len(field_names)))

    # vote for fields based on valid tickets
    for valid_ticket in valid_tickets:
        numbers = [int(n) for n in valid_ticket.split(',')]
        for i in range(len(numbers)):
            for field in fields:
                if field.in_ranges(numbers[i]):
                    field.vote(i)

    # determine field positions based on scores and where the max is in the score rows
    scores = np.array([field.score for field in fields])

    mask = np.ones(scores.shape[1])

    while True:
        for i in range(scores.shape[0]):
            if fields[i].position is not None:
                continue
            array = scores[i, :] * mask
            unique, counts = np.unique(array, return_counts=True)
            occurrences = dict(zip(unique, counts))

            maximum = np.max(array)

            num_of_occurrences = occurrences[maximum]

            if num_of_occurrences == 1:
                argmax = np.argmax(array)
                fields[i].set_position(argmax)
                mask[argmax] = 0

        if np.sum(mask) == 0:
            break

    for field in fields:
        print('Name {:30s} Position {:10d}'.format(field.name, field.position + 1))

    # get my ticket
    for line in notes[notes.find('your ticket:') + len('your ticket:'):notes.find('nearby tickets:')].split('\n'):
        # if line is not empty
        if line:
            my_ticket = line.split(',')
            # print(my_ticket)

    print()
    product = 1
    for field in fields:
        if field.name.split(' ')[0] == 'departure':
            # print(field.name)
            product *= int(my_ticket[field.position])

    print('Product = {:d}'.format(product))
