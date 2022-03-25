from turtle import right


with open("./puzzle.txt") as file:
    puzzle = [[int(number) for number in line]
              for line in file.read().splitlines()]


# for line in puzzle:
#     print(line)




print("Part 1")

def find_point(i, j):
    if i == -1 or j == -1:
        return 9
    try:
        return puzzle[i][j]
    except:
        return 9

points = []
positions = []

i = 0
for line in puzzle:
    j = 0
    for number in line:
        up = find_point(i-1, j)
        down = find_point(i+1, j)
        left = find_point(i, j-1)
        right = find_point(i, j+1)

        if number < up and number < down and number < left and number < right:
            positions.append([i, j])
            points.append(number)
        j += 1
    i += 1

print("Sum of Risk Levels:", sum(points)+len(points))

# ===================== PART 2 =======================================
print('Part 2')

def find_basin(position, collector=[],size=1):
    i, j = position
    number=find_point(i,j)
    # Finding points (up,down,left and right, in this order)
    points = []
    points.append([i-1, j])
    points.append([i+1, j])
    points.append([i, j-1])
    points.append([i, j+1])

    for point in points:
        x,y = point
        p_number=find_point(x,y)
        if x>=0 and y>=0:
            try:
                if p_number != 9 and p_number == number+1 and point not in collector:
                    print("Position",position,"Point",point,"Number",puzzle[x][y])
                    collector.append(point)
                    size = find_basin([x,y],collector,size+1)
            except:
                
                pass
    return size

basins = []
f_basins =[]

# Finding Basins
for position in positions:
    print("Position:", position)
    basins.append(find_basin(position,[]))
    # print("Size:", basins[-1])

# Filtering 3 higher basins
for i in range(0,3):
    f_basins.append(max(basins))
    basins.remove(max(basins))

print("Multiplying:",f_basins[0]*f_basins[1]*f_basins[2])