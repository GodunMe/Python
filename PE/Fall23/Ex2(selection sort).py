def selection_sort():
    file_name = "numbers.txt"
    file = open(file_name, "r")
    nums = []
    for line in file:
        nums.extend(map(int,line.split()))
    for i in range(len(nums)):
        max_index = i
        for j in range(i+1, len(nums)):
            if nums[j] > nums[max_index]:
                max_index = j
        nums[i], nums[max_index] = nums[max_index], nums[i]
    return nums

print(selection_sort())
