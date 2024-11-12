# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

def find_longest_common_prefix(strs):
    if not strs:
        return ""
    
    common = ""
    strs.sort()
    first = strs[0]
    last = strs[-1]
    
    for i in range(len(first)):
        if i < len(last) and first[i] == last[i]:
            common += first[i]
        else:
            break 
    
    return common
# user_input = input("Enter strings: ")
# strs = user_input.split() 
strs = ["flower", "flow", "flight"]
longest_common = find_longest_common_prefix(strs)
if longest_common == "":
    print('""') 
else:
    print((f'"{longest_common}"'))
