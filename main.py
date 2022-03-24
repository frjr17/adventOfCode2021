
with open("./input.txt") as file:
    puzzle = file.read().splitlines()
    puzzle = [[word.strip() for word in line.split("|")] for line in puzzle]


part = '2'
if part == '1':
    print("Part 1")
    acc = 0
    right_puzzle = [word for line in puzzle for word in line[1].split(" ")]
    default = {2: 1, 4: 4, 3: 7, 7: 8}

    for word in right_puzzle:
        if len(word) in default.keys():
            acc += 1

    print('Instances:', acc)
else:
    print('Part 2')
    
        