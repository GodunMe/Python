# Have the function ArrayAdditionI(arr) take the array of numbers stored in arr and return the string True
# if any combination of numbers in the aray (excluding the largest number) can be added up to equal the largest number in the array,otherwise return the string False.
# For example: if arr contains [4, 6, 23, 10, 1, 3] the output should return True because 4+6+10+3=23.
# The array will not be empty, will not contain all the same ele, and may contain negative numbers.

def ArrayAdditionI(arr):
    max_num = max(arr)
    arr.remove(max_num)
    if can_add_to_target(arr, max_num):
        return True
    else:
        return False


def can_add_to_target(arr, target):
    length = len(arr)
    #Recursive to check all posible combination
    def backtrack(index, sum):
        if index == length or sum > target or target == 0:
            return False
        if sum == target:
            return True
        if backtrack(index+1, sum):
            return True
        if backtrack(index+1, sum + arr[index]):
            return True
        
    return backtrack(0, 0)

while True:
    try:
        arr = list(map(int, input("Enter the array: ").split()))
        #Check empty array and contain all the same ele
        if len(arr) == 0 or len(set(arr)) == 1:
            raise ValueError("The array will not be empty, will not contain all the same ele, and may contain negative numbers. Pls enter again.")
        break
    except ValueError as e:
        print(e)
print(f'Output: {ArrayAdditionI(arr)}')