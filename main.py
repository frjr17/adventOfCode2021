import numpy as np
import math
with open("./input.txt") as file:
    puzzle = file.read().splitlines()[0]
    puzzle = [int(number) for number in puzzle.split(",")]

part = '2'
if part == '1':
    print("Part 1")
    positions = puzzle
    fuel = 0
    selected_position = 0

    for position in positions:
        fuel_required = 0
        i = 0
        for number in puzzle:
            fuel_required += abs(number - position)
        if fuel_required < fuel or fuel == 0:
            fuel = fuel_required
            selected_position = position

    print('Total Cost:', fuel, "Position:", selected_position)

else:
    print('Part 2')
    positions = puzzle
    fuel = 0

    position = np.mean(puzzle)
    position = math.floor(position) if position-int(position)<=0.6 else math.ceil(position)

    for number in puzzle:
        steps = abs(number-position)
        for i in range(1,steps+1):
            fuel +=i

    print('Total Cost:', fuel)