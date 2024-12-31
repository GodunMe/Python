#Write a program that ask the user for a range (start and end) and the number of unique integers they want to generate.
#The program should then generate that many integers and store them in a list.
#Display a list, the avg, and the minimum value.

import random
def get_input():
    while True:
        try:
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the sendart of the range: "))
            length = int(input("How many unique integers would you like to generate? "))
            if start < end and (end-start+1) >= length > 0:
                return start, end, length
        except ValueError as e:
            print("Enter the integer number.")

def generate_list(start, end, length):
    random_list = set()
    while len(random_list) < length:
        random_num = random.randint(start, end)
        random_list.add(random_num)
    return random_list

def main():
    start, end, length = get_input()
    random_list = generate_list(start, end, length)
    avg = sum(random_list) / len(random_list)
    minimum = min(random_list)
    print("Generated list of unique integers: [" + ", ".join(map(str, random_list)) + "]")
    print(f"Average of the integers: {avg:.2f}")
    print(f"Minimum value in the list: {minimum}")

main()