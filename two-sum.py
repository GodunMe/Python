# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

def find_position(array, target):
    #Loop from the first ele to the last ele
    for i in range(len(array)):
        #Loop from the last to the first
        for j in range(len(array) - 1, i, -1):
            if array[i] + array[j] > target:
                continue
            elif array[i] + array[j] < target:
                continue
            else:
                return i, j
    return -1, -1  

nums = [3, 2, 4]
target = 6
[first, last] = find_position(nums, target)
if first == -1 and last == -1:
    print("Can't find out.")
else:
    print(f"[{first}, {last}]")
