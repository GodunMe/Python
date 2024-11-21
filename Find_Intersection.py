# Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: 
# the first element will represent a list of comma-separated numbers sorted in ascending order, 
# the second element will represent a second list of comma-separated numbers (also sorted). 
# Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. 
# If there is no intersection, return the string false.

def FindIntersection(strArr):

  # code goes here
  list1 = list(map(int, strArr[0].split(',')))
  list2 = list(map(int, strArr[1].split(',')))
  i = j = 0
  Intersection = []
  while i < len(list1) and j < len(list2):
    if list1[i] == list2[j]:
      Intersection.append(list1[i])
      i += 1
      j += 1
    elif list1[i] < list2[j]:
      i += 1
    else:
      j += 1
  return Intersection

# keep this function call here 
print(FindIntersection(input()))