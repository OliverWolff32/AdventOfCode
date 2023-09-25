abcs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def first_half():
    sum = 0
    with open('prob3.txt') as file:
        for line in file:
            h1 = line[0:int(len(line)/2)]
            h2 = line[int(len(line)/2):]
            for char in h2:
                if char in h1:
                    sum += abcs.index(char) + 1
                    break
    return sum
    
def second_half():
    sum = 0
    with open('prob3.txt') as file:
        lines = []
        for line in file:
            lines.append(line.strip())
            if len(lines) == 3:
                for char in lines[0]:
                    if char in lines[1] and char in lines[2]:
                        sum += abcs.index(char) + 1
                        break
                lines = []
    return sum
    
print(f"first half:", first_half())
print(f"second half:", second_half())

            

