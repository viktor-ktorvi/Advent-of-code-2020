import numpy as np
from day12.part1 import TRANSLATION2ANGLES, ROTATION2DIRECTIONS


class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0

        self.waypoint_x = 10
        self.waypoint_y = 1

    def execute_instructions(self, instructions):

        # analize instructions and execute them one by one

        for instruction in instructions:
            action = instruction[0]
            value = int(instruction[1:])

            self.execute_action(action, value)

    def execute_action(self, action, value):

        # determine what sort of action is to be done and move in an appropriate way

        if action in ROTATION2DIRECTIONS.keys():
            angle = value * ROTATION2DIRECTIONS[action] * np.pi / 180

            v = np.array([self.waypoint_x, self.waypoint_y]).reshape(2, 1)
            R = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])

            v_rotated = R @ v
            self.waypoint_x = v_rotated[0]
            self.waypoint_y = v_rotated[1]
            return

        if action in TRANSLATION2ANGLES.keys():
            angle = TRANSLATION2ANGLES[action] * np.pi / 180
            self.waypoint_x += int(np.cos(angle) * value)
            self.waypoint_y += int(np.sin(angle) * value)

            return

        elif action == 'F':
            self.x += self.waypoint_x * value
            self.y += self.waypoint_y * value

        else:
            raise ValueError("Unrecognized action " + action)

    def manhattan(self):
        # L1 norm: sum |x_i| for all i
        return np.abs(self.x) + np.abs(self.y)


if __name__ == '__main__':
    f = open('my_instructions.txt', 'r')
    instructions_str = f.read()
    f.close()

    # instructions_str = input()
    instructions = instructions_str.split('\n')

    ship = Ship()
    ship.execute_instructions(instructions)

    print('The Manhattan distance is: ', ship.manhattan())
