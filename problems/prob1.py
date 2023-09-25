def main():
    biggest = 0
    bigger = 0
    big = 0
    with open('prob1.txt') as file:
        total = 0
        for line in file:
            if line.splitlines()[0] == "":
                #print(total)
                nums = insert_new(total, biggest, bigger, big)
                biggest = nums[0]
                bigger = nums[1]
                big = nums[2]
                total = 0
            else:
                total += int(line.splitlines()[0])
    print(biggest + bigger + big)

def insert_new(a, biggest, bigger, big):
    if(a > big):
        if(a > bigger):
            if(a > biggest):
                big = bigger
                bigger = biggest
                biggest = a
            else:
                big = bigger
                bigger = a
        else:
            big = a
    
    return (biggest, bigger, big)
main()
