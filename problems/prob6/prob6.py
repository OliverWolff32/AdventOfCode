last_four = []

def main():
    with open("prob6input.txt") as file: 
        string = file.read().strip()
        for i in range(0,len(string)-1): 
            c = string[i]
            if(len(last_four)!= 4):
                if c not in last_four: 
                    return i+1
                else:
                    last_four.append(c)
            else: 
                if c in last_four: 
                    cycleArray(last_four, c)
                else:
                    return i+1

def cycleArray(arr, append):
    arr.append(append)
    arr = arr[1:]

print(main())