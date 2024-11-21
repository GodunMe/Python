# Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:

# 1. The username is between 4 and 25 characters.
# 2. It must start with a letter.
# 3. It can only contain letters, numbers, and the underscore character.
# 4. It cannot end with an underscore character.

# If the username is valid then your program should return the string true, otherwise return the string false.

def CodelandUsernameValidation(strParam):
  # code goes here
  if not 4 <= len(strParam) <= 25:
    return False
  if strParam[-1] == '_':
    return False
  if not strParam[0].isalpha:
    return False
  if not all(char.isalnum or char == '_' for char in strParam):
    return False
  return True

# keep this function call here 
print(CodelandUsernameValidation(input()))