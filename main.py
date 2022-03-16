
with open("./puzzle.txt") as file:
    puzzle = file.read().splitlines()
    # print(puzzle)


resp = input("Part 1 or 2?")

if resp == '1':
    print("Part 1")
    dict1 = {}
    incr = 0
    decr = 0
    i = 0
    for number in puzzle:
        if i != 0:
            before_number = puzzle[i-1]
            if number > before_number:
                print(number,'increased from', before_number)
                dict1[number] = 'increased'
                incr+=1
            else:
                print(number,'decreased from', before_number)
                dict1[number] = 'decreased'
                decr+=1
        i+=1


    print('Increased:', incr, '. Decreased:', decr)

else:
    pass
