nums = []
total = 0
with open("OliverProb4Input.txt") as file:
    total = 0
    for line in file: 
        numIdx = 0
        nums = []
        for item in line.split(","):
            for num in item.split("-"):
                nums.append(int(num.strip()))
        if(nums[3] <= nums[1] and nums[3] >= nums[0]):
            total += 1
        elif(nums[2] <= nums[1] and nums[2] >= nums[0]):
            total += 1
        elif(nums[0] <= nums[3] and nums[0] >= nums[2]):
            total += 1
        elif(nums[1] <= nums[3] and nums[1] >= nums[2]):
            total += 1
print(total)