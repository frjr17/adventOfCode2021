with open("./puzzle.txt") as file:
    puzzle = file.read().splitlines()

    puzzle = [[[int(coord) for coord in coords.split(',')]
               for coords in line.split(' -> ')]
              for line in puzzle]

    max_number = max([coord for line in puzzle
                      for coords in line
                      for coord in coords])+1

    diagram = [('. '*max_number).strip().split(' ')
               for x in range(0, max_number)]

    # for line in diagram:
    #     print(line)


part = '1'
if part == '1':
    print("Part 1")
    overlaps = 0
    for line in puzzle:
        x1, y1 = line[0]
        x2, y2 = line[1]
        points = []
        x_range = range(min(x1, x2), max(x1, x2)+1)
        y_range = range(min(y1, y2), max(y1, y2)+1)
        
        if x1 == x2 or y1 == y2:
            for x in x_range:
                for y in y_range:
                    point = [x, y]
                    if point not in points:
                        points.append(point)

        for point in points:
            print(point)
            x, y = point

            if diagram[y][x] == '.':
                diagram[y][x] = 1
            
            if diagram[y][x] >= 1:
                diagram[y][x] += 1
                overlaps += 1

    diagram = [[str(point) for point in line] for line in diagram]

    print('Final Diagram')
    for line in diagram:
        print(line)
    print('\n Overlaps:',overlaps)
else:
    print('Part 2')
