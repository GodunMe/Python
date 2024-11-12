def Check_Palindrome_Number(number):
    if number < 0:
        return False
    else:
        str_num = str(number)
        return str_num == str_num[::-1]

number = int(input("Enter number you want to check: "))
print(Check_Palindrome_Number(number))