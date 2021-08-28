import numpy as np

TRANSLATION2ANGLES = {
    'N': 90,
    'S': -90,
    'E': 0,
    'W': 180
}

ROTATION2DIRECTIONS = {
    'L': 1,
    'R': -1
}


class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0

    def execute_instructions(self, instructions):

        # analize instructions and execute them one by one

        for instruction in instructions:
            action = instruction[0]
            value = int(instruction[1:])

            self.execute_action(action, value)

    def execute_action(self, action, value):

        # determine what sort of action is to be done and move in an appropriate way

        if action in ROTATION2DIRECTIONS.keys():
            self.angle += ROTATION2DIRECTIONS[action] * value
            return

        if action in TRANSLATION2ANGLES.keys():
            angle = TRANSLATION2ANGLES[action] * np.pi / 180
        elif action == 'F':
            angle = self.angle * np.pi / 180
        else:
            raise ValueError("Unrecognized action " + action)

        self.x += int(np.cos(angle) * value)
        self.y += int(np.sin(angle) * value)

    def manhattan(self):
        # L1 norm: sum |x_i| for all i
        return np.abs(self.x) + np.abs(self.y)


if __name__ == '__main__':
    # f = open('example_instructions.txt', 'r')
    # instructions_str = f.read()
    # f.close()

    instructions_str = input()
    instructions = instructions_str.split('\n')

    ship = Ship()
    ship.execute_instructions(instructions)

    print('The Manhattan distance is: ', ship.manhattan())
