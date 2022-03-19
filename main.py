with open("./puzzle.txt") as file:
    fpuzzle = file.read().splitlines()

    # print(puzzle)


resp = 2

puzzle = [[number for number in binary] for binary in fpuzzle]


def get_positions(puzzle):
    positions = {}
    i = 0
    for binary in puzzle:
        j = 0
        for number in binary:
            try:
                positions[j] += number
            except KeyError:
                positions[j] = number
            j += 1

        i += 1
    return positions

def get_rating(puzzle,number,i,reverse):
    rating = []
    comp_num = '1' if not reverse == True else '0'
    print(comp_num)
    comp_num_r = '0' if not reverse == True else '1'
    if number.count('1')>= number.count('0'):
        for binary in puzzle:
            if binary[i] == comp_num:
                rating.append(binary)
    else:
        for binary in puzzle:
            if binary[i] == comp_num_r:
                rating.append(binary)
    return rating
        
if resp == '1':
    print("Part 1")
    gamma_rates = []
    epsilon_rates = []
    positions = get_positions(puzzle)
    for i, number in positions.items():
        if number.count('1') > number.count("0"):
            gamma_rates.append('1')
            epsilon_rates.append('0')
        else:
            gamma_rates.append('0')
            epsilon_rates.append('1')
    gamma = ''.join(gamma_rates)
    epsilon = ''.join(epsilon_rates)
    print(f"Gamma: {gamma} = {int(gamma,2)}")
    print(f"Epsilon: {epsilon} = {int(epsilon,2)} ")
    print(f"Power Consumption: {int(gamma,2)*int(epsilon,2)}")
else:
    print('Part 2')
    o_puzzle = fpuzzle
    o_rating = []
    c_puzzle = fpuzzle
    c_rating = []
    for i in range(0, len(fpuzzle[0])):
        o_number = get_positions(o_puzzle)[i]
        c_number = get_positions(c_puzzle)[i]
        o_rating = get_rating(o_puzzle,o_number,i,False)
        c_rating = get_rating(c_puzzle,c_number,i,True)
        if len(o_puzzle) > 1:
            o_puzzle = o_rating
            o_rating =[]
        if len(c_puzzle) > 1:
            c_puzzle = c_rating
            c_rating =[]
    o_rating = int(o_puzzle[0],2)
    c_rating = int(c_puzzle[0],2)
    print(f'Oxygen rating: {o_rating}')
    print(f'CO2 rating: {c_rating}')
    print(f'Life Support Rating: {o_rating*c_rating}')