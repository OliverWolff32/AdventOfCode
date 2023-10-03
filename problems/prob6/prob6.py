

def part1():
    last_four = []
    with open("/Users/oliverwolff/Desktop/CS 3:4/advent-of-code-template/problems/prob6/prob6input.txt") as file: 
        string = file.read().strip()
        for i in range(0,len(string)-1): 
            c = string[i]
            if(len(last_four)!= 4):
                last_four.append(c)
            elif has_duplicates(last_four): 
                last_four = cycleArray(last_four, c)
                if i < 10 : 
                    print(last_four)
                elif not has_duplicates(last_four):
                    return i+1

def part2():
    last_fourteen = []
    with open("/Users/oliverwolff/Desktop/CS 3:4/advent-of-code-template/problems/prob6/prob6input.txt") as file: 
        string = file.read().strip()
        for i in range(0,len(string)-1): 
            c = string[i]
            if(len(last_fourteen) < 14):
                last_fourteen.append(c)
            elif has_duplicates(last_fourteen): 
                last_fourteen = cycleArray(last_fourteen, c)
                if i == 15 : 
                    print(last_fourteen)
                elif not has_duplicates(last_fourteen):
                    return i+1


def cycleArray(arr, append):
    arr.append(append)
    arr = arr[1:]
    return arr

def has_duplicates(list): 
    return len(list) != len(set(list))

print(part1())
print(part2())