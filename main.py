
from ast import Break
from select import select


def filter_list(arr):
    return list(filter(None, arr))


def get_rows(chart):
    return [filter_list(row.split(' ')) for row in chart]


def get_colums(chart):
    columns = [[row[i] for row in chart] for i in range(0, 5)]
    return columns


def print_line(l):
    for x in l:
        print(x)
    print("\n")


def detect(chart, numbers_played):
    rows = chart
    selected = None
    filtered_list = None
    columns = get_colums(chart)

    for row in rows:
        if set(row) <= set(numbers_played):
            # print("row:",row)
            selected = row
            break
    for column in columns:
        if set(column) <= set(numbers_played):
            # print("column:",column)
            selected = column
            break

    if selected:
        filtered_list = filter_chart(chart,numbers_played)
    
    return [selected, filtered_list,chart]

def filter_chart(chart,numbers_played):
    flat_list = [number for line in chart for number in line]
    filtered_list = []
    for number in flat_list:
        if number not in numbers_played:
            filtered_list.append(number)
    return filtered_list

with open("./puzzle.txt") as file:
    puzzle = file.read().splitlines()
    numbers = puzzle[0].split(",")
    bingo_charts = filter_list([lines for lines in puzzle[2:]])
    bingo_charts = filter_list([bingo_charts[i:i+5]
                               for i in range(0, len(bingo_charts), 5)])
    bingo_charts = [[[number for number in filter_list(
        line.strip().split(" "))]for line in chart] for chart in bingo_charts]

part = '2'
if part == '1':
    print("Part 1")

    for i in range(0, len(numbers)):
        for j in range(0, len(bingo_charts)):
            selected, ulist = detect(
                filter_list(bingo_charts[j]), numbers[0:i])
            j += 1
            if selected:
                break
        if selected:
            break
        i += 1

    last_number = numbers[0:i][-1]
    print('Winner Row:', selected)
    print('Last Number:', last_number)

    sum = 0
    for number in ulist:
        sum += int(number)

    print("Final Score:", int(last_number)*int(sum))

else:
    print('Part 2')
    filtered_charts = bingo_charts
    i = 0
    while True:
        for j in range(0, len(bingo_charts)):
            selected, ulist, chart = detect(filter_list(
                filtered_charts[j]), numbers[0:i])
            if selected:
                print(len(filtered_charts))
                if len(filtered_charts) >= 1:
                    filtered_charts.remove(filtered_charts[j])
                break
            j += 1
        if selected and len(filtered_charts) < 1:
            break
        i += 1
        if i == len(numbers)-1:
            i=0
    last_number = numbers[0:i][-1]
    print('Charts Available:',len(filtered_charts))
    print('Last Row:', selected)
    print('Last Chart:')
    print_line(chart)
    print('Last Number:', last_number)
    print('Unused numbers:',ulist)
    sum = 0
    for number in ulist:
        sum += int(number)

    print("Final Score:", int(last_number)*int(sum))