with open("./puzzle.txt") as file:
    puzzle = file.read().splitlines()
    # print(puzzle)


resp = input("Part 1 or 2?")

if resp == '1':
    print("Part 1")
    horizontal_position = 0
    depth = 0

    for direction in puzzle:
        word, number = direction.split(" ")
        if word == 'forward':
            horizontal_position = horizontal_position + int(number)
        if word == 'down':
            depth = depth + int(number)
        if word == 'up':
            depth = depth - int(number)

    print('Horizontal position:', horizontal_position)
    print('Depth:', depth)
    print('Mix:', depth*horizontal_position)

else:
    print('Part 2')
    horizontal_position = 0
    depth = 0
    aim = 0
    for direction in puzzle:
        word, number = direction.split(" ")
        if word == 'forward':
            horizontal_position = horizontal_position + int(number)
            depth = depth + aim * int(number)
        if word == 'down':
            aim = aim + int(number)
        if word == 'up':
            aim = aim - int(number)
        # print(horizontal_position,depth,aim)

    print('Horizontal position:', horizontal_position)
    print('Depth:', depth)
    print('Aim:', aim)
    print('Mix:', depth*horizontal_position)
