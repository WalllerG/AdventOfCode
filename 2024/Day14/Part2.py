import re
from Util.util import read_input

class Tile:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def move(self):
        new_x = self.position[0] + self.velocity[0]
        new_y = self.position[1] + self.velocity[1]
        if new_x < 0:
            new_x = 101 + new_x
        elif new_x >= 101:
            new_x = new_x - 101

        if new_y < 0:
            new_y = 103 + new_y
        elif new_y >= 103:
            new_y = new_y - 103

        self.position = (new_x, new_y)

data = read_input(14,True)

robots = []
for line in data:
    p_v = line.split()
    pos = list(map(int, re.findall(r"(-?\d+)", p_v[0])))
    vol = list(map(int, re.findall(r"(-?\d+)", p_v[1])))
    robots.append(Tile(pos, vol))
num_robots = len(robots)

seconds = 0
while True:
    seconds += 1
    robot_set = set()

    for robot in robots:
        robot.move()
        robot_set.add(robot.position)

    if len(robot_set) == num_robots:
        print(f"Christmas Tree found at: {seconds}")
        break



