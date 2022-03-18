'''
Now, you need to figure out how to pilot this thing.

It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.

Note that since you're on a submarine, down and up affect your depth, and so they have the opposite 
result of what you might expect.

The submarine seems to already have a planned course (your puzzle input). You should probably figure 
out where it's going. For example:

forward 5
down 5
forward 8
up 3
down 8
forward 2

Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

forward 5 adds 5 to your horizontal position, a total of 5.
down 5 adds 5 to your depth, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13.
up 3 decreases your depth by 3, resulting in a value of 2.
down 8 adds 8 to your depth, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15.

After following these instructions, you would have a horizontal position of 15 and a depth of 10. 
(Multiplying these together produces 150.)

Calculate the horizontal position and depth you would have after following the planned course. 
What do you get if you multiply your final horizontal position by your final depth?
'''

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
    print('Part 2')
    windows = {}
    incr = 0
    decr = 0
    i = 0
    for number in puzzle:
        windows[i] = {}
        if i !=0:
            try:
                number2 = puzzle[i+1]
                number3 = puzzle[i+2]
                windows[i]['quantity'] = int(number)+int(number2)+int(number3)
                if windows[i]['quantity'] > windows[i-1]['quantity']:
                    windows[i]['status'] = 'increased'
                    incr+=1
                else:
                    windows[i]['status'] = 'decreased'
                    decr+=1
            except IndexError:
                break
        else:
            windows[i]['quantity'] = 0
        i+=1
    print('Increased:',incr,'. Decreased:',decr)


