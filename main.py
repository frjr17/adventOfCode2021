


with open("./input.txt") as file:
    puzzle = file.read().splitlines()
    puzzle = [[word.strip() for word in line.split("|")] for line in puzzle]


right_puzzle = [word for line in puzzle for word in line[1].split(" ")]
default = {2: 1, 4: 4, 3: 7, 7: 8}

def find_word(pattern, words):
    selected = ''
    for word in words.split(" "):
            acc =0
            for letter in word:
                if letter in pattern:
                    acc+=1
                if acc == len(pattern):
                    selected = word
                    break
    return selected


part = '2'
if part == '1':
    print("Part 1")
    acc = 0

    for word in right_puzzle:
        if len(word) in default.keys():
            acc += 1

    print('Instances:', acc)
else:
    print('Part 2')
    left_puzzle = [[word for word in line[0].split(" ")] for line in puzzle ]
    numbers = []
    for line in puzzle:
        ref = {}
        left = line[0].split(" ")
        left_d = {len(i):" " for i in left}
        for word in left:
            left_d[len(word)] += " " + word
            left_d[len(word)] = left_d[len(word)].strip()
        ref[left_d[2]] = 1
        ref[left_d[4]] = 4
        ref[left_d[3]] = 7
        ref[left_d[7]] = 8

        # Finding three
        three = find_word(left_d[2],left_d[5])
        ref[three] = 3
        
        # Finding nine
        nine = find_word(three,left_d[6])
        ref[nine] = 9    
        
        #Finding zero
        zero_search = ' '.join([word for word in left_d[6].split(" ") if word != nine])
        zero = find_word(left_d[3],zero_search)
        ref[zero] = 0
        # After zero, six comes by default
        six = [word for word in left_d[6].split(" ") if word != nine and word != zero][0]
        ref[six] = 6

        # Finding five
        five_search = ' '.join([word for word in left_d[5].split(" ") if word != three])
        for word in five_search.split(" "):
            acc =0
            selected = ''
            for letter in word:
                if letter in nine:
                    acc +=1
                if acc == len(nine)-1:
                    selected = word
                    break
            if selected:
                break
        five =  selected
        ref[five] = 5
        # After five, 2 comes by default
        two = ' '.join([word for word in left_d[5].split(" ") if word != three and word != five])
        ref[two] = 2

        # Adding values from right line
        right = line[1].split(" ")
        number = ''
        for word in right:
            selected = find_word(word,left_d[len(word)])
            number+= str(ref[selected])
       
        numbers.append(int(number))
    
    print('Add UP:',sum(numbers))