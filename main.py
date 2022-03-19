
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


def detect_row_column(chart, numbers_played):
    # Detect Rows
    rows = chart
    selected=None
    filtered_list = None
    # Detect Columns
    columns = get_colums(chart)
    # Detect if there are mathed rows
    for row in rows:
        if set(row) <= set(numbers_played):
            # print('Row',row)
            selected = row
            break
    for column in columns:
        if set(column) <= set(numbers_played):
            # print('Row',row)
            selected = column
            break
    if selected:
        flat_list = [number for line in chart for number in line]
        filtered_list = []
        for number in flat_list:
            if number not in numbers_played:
                filtered_list.append(number)
    return [selected,filtered_list]


with open("./puzzle.txt") as file:
    puzzle = file.read().splitlines()
    numbers = puzzle[0].split(",")
    bingo_charts = filter_list([lines for lines in puzzle[2:]])
    bingo_charts = filter_list([bingo_charts[i:i+5] for i in range(0,len(bingo_charts),5)])
    bingo_charts = [[[number for number in filter_list(line.strip().split(" "))]for line in chart] for chart in bingo_charts]
        # chart = puzzle[i:i+5]
        # arr_chart = [[number for number in filter_list(line.strip().split(" "))] for line in chart]
        # arr_chart = filter_list(arr_chart)
        # bingo_charts.append(arr_chart)
       
part = '1'
if part == '1':
    print("Part 1")

    for i in range(0,len(numbers)):
       
        for j in range(0,len(bingo_charts)):
            # print('Bingo Chart')
            # print(j)
            # print_line(bingo_charts[j])
            # print('Numbers')
            selected,ulist = detect_row_column(filter_list(bingo_charts[j]),numbers[0:i])
            j+=1
            if selected:
                break
        if selected:
            break
        i+=1
    last_number = numbers[0:i][-1]
    print('Winner Row:',selected)
    print('Last Number:',last_number)
    sum = 0
    # Missing numbers unselected
    for number in ulist:
        sum += int(number)
    print("Final Score:",int(last_number)*int(sum))

else:
    print('Part 2')
