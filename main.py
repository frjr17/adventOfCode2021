
with open("./input.txt") as file:
    puzzle = file.read().splitlines()
    puzzle = [int(number) for line in puzzle for number in line.split(",")]


part = '2'
if part == '1':
    print("Part 1")
    day =puzzle
    days = 0
  
    for i in range(0, 256):
        print(i)
        day = [number-1 for number in day]
        j = 0
        if -1 in day:
            occurrences = day.count(-1)
            if occurrences:
                day.extend([8]*occurrences)
            day = [6 if number == -1 else number for number in day]
            


    print('Fishes:', len(day))
else:
    print('Part 2')
    from collections import Counter
    data1 = puzzle
    lifes = dict(Counter(data1))

    days = 256
    for day in range(1, days+1):
        lifes = {l: (0 if lifes.get(l+1) is None else lifes.get(l+1)) for l in range(-1, 8)}
        # make all 8s -1 because we create new fish with 8 after it reaches 0
        lifes[8] = lifes[-1]
        # add new lifes to that are exhausted
        lifes[6] += lifes[-1]
        # reset exhausted lifes
        lifes[-1] = 0 

    print(sum(lifes.values()))