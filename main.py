with open("./input.txt") as file:
    puzzle = file.read().splitlines()

    puzzle = [[[int(coord) for coord in coords.split(',')]
               for coords in line.split(' -> ')]
              for line in puzzle]

    max_number = max([coord for line in puzzle
                      for coords in line
                      for coord in coords])+1

    diagram = [('. '*max_number).strip().split(' ')
               for _ in range(0, max_number)]

    # for line in diagram:
    #     print(line)


part = '2'
if part == '1':
    print("Part 1")
    overlaps = 0

    for line in puzzle:
        x1 = min(line[0][0], line[1][0])
        y1 = min(line[0][1], line[1][1])
        x2 = max(line[0][0], line[1][0])
        y2 = max(line[0][1], line[1][1])
        
        x_range = range(x1, x2+1)
        y_range = range(y1, y2+1)
        points = []
        
        if x1 == x2 or y1 == y2:
            for x in x_range:
                for y in y_range:
                    point = [x, y]
                    points.append(point)

        for point in points:
            y, x = point
            d = diagram[x][y]
            if d == '.':
                diagram[x][y] = 1
            else:
                diagram[x][y] += 1
            if d == 1:
                overlaps += 1

    # Stringifying for estetics
    # diagram = [' '.join([str(point) for point in line]) for line in diagram]

    # for line in diagram:
    #     print(line)

    print("Overlaps:", overlaps)

else:
    print('Part 2')
    overlaps = 0

    for line in puzzle:
        points = []
        x1 = min(line[0][0], line[1][0])
        y1 = min(line[0][1], line[1][1])
        x2 = max(line[0][0], line[1][0])
        y2 = max(line[0][1], line[1][1])
        
        x_range = range(x1, x2+1)
        y_range = range(y1, y2+1)
        
        if x1 == x2 or y1 == y2:
            for x in x_range:
                for y in y_range:
                    point = [x, y]
                    points.append(point)

        else:
            x1 = line[0][0]
            x2 = line[1][0]
            y1 = line[0][1]
            y2 = line[1][1]

            x_range = range(x1, x2-1 if x1 > x2 else x2 + 1,
                            1 if x1 < x2 else -1)
            y_range = range(y1, y2-1 if y1 > y2 else y2 + 1,
                            1 if y1 < y2 else -1)

            for x, y in zip(x_range, y_range):
                point = [x, y]
                points.append(point)

        for point in points:
            y, x = point
            d = diagram[x][y]

            if d == '.':
                diagram[x][y] = 1
            else:
                diagram[x][y] += 1
            if d == 1:
                overlaps += 1

    # Stringifying for estetics
    # diagram = [' '.join([str(point) for point in line]) for line in diagram]

    # for line in diagram:
    #     print(line)

    print("Overlaps:", overlaps)
