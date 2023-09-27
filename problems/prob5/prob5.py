import re

def first_half():
    strinc = ''
    with open('prob5.txt') as file:
        lines = [line for line in file]
        arrays = [[],[],[],[],[],[],[],[],[]]
        crates = lines[:lines.index('\n')-1]
        instructions = lines[lines.index('\n')+1:]
        for line in crates:
            for i in range(1, len(line), 4):
                if(line[i] != " "):
                    arrays[int(i/4)].append(line[i])
        for line in instructions:
            moves = re.findall(r'[0-9]+', line)
            moves = [int(move) for move in moves]
            boxes = []
            for i in range(moves[0]):
                arrays[moves[2]-1].insert(0, arrays[moves[1]-1].pop(0))
        for arr in arrays:
            strinc = strinc + arr[0]
        print(arrays)
    return strinc

def second_half():
    strinc = ''
    with open('prob5.txt') as file:
        lines = [line for line in file]
        arrays = [[],[],[],[],[],[],[],[],[]]
        crates = lines[:lines.index('\n')-1]
        instructions = lines[lines.index('\n')+1:]
        for line in crates:
            for i in range(1, len(line), 4):
                if(line[i] != " "):
                    arrays[int(i/4)].append(line[i])
        for j,line in enumerate(instructions):
            moves = re.findall(r'[0-9]+', line)
            moves = [int(move) for move in moves]
            boxes = []
            for i in range(moves[0]):
                boxes.append(arrays[moves[1]-1].pop(0))
            for box in reversed(boxes):
                arrays[moves[2]-1].insert(0, boxes.pop())
        for arr in arrays:
            strinc = strinc + arr[0]
    return strinc
    

print(first_half())
print(second_half())
