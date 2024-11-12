def roman_convert(s):
    #Dictionary Roman value
    roman_values = { 'I':1, 'V':5,'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    previous_value = 0
    total = 0

    for char in s:
        current_value = roman_values[char]
        if current_value > previous_value:
            total += current_value - 2*previous_value
        else: 
            total += current_value
        previous_value = current_value
    
    return total

roman_value = input("Enter roman value: ")
integer_value = roman_convert(roman_value)
print(f"The integer value of {roman_value} is: {integer_value}")