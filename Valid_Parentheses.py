# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.
# Có tham khảo ChatGPT

def check_valid(s):
    stack = []
    map = {')' : '(', '}' : '{', ']' : '['}
    
    for char in s:
        #Check char is close bracket
        if char in map:
            #check stack empty
            if stack:
                top_ele = stack.pop()
            else:
                return False
            if map[char] != top_ele:
                return False
        #Char is open bracket
        else:
            stack.append(char)
    return True
s = "'(){}['"
print(check_valid(s))