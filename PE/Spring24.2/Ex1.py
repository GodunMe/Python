#Write a program that ask user how many integers they want to generate.
#It should then generate that many integer randomly which is range from 1 to 100 and then store in a list.
#After list is populated, the program will calculate and display the average of these numbers, and also display the smallest and highest value in the list.

import random

def get_input():
    while(1):
        try:
            num_integer = int(input("How many random integers would you like to generate? "))
            if (num_integer > 0):
                return num_integer
            else:
                print("Please enter a positive integer.")
        except ValueError as e:
            print("Invalid input. Please enter a positive integer.")
        
def generate_list(lower, upper, length):
    random_list = []
    for i in range(length):
        random_num = random.randint(lower, upper)
        random_list.append(random_num)
    return random_list
    #return [random.randint(lower, upper) for i in range(length)]

    #Nếu đề yêu cầu các phần tử phải unique
    #random_list = set()
    #while len(random_list) < length:
        # random_num = random.randint(lower, upper)
        # random_list.add(random_num)

def do_thing(list):
    max_num = max(list)
    min_num = min(list)
    avg = sum(list) / len(list)
    print("Generated list of integers: ", list)
    print(f"Avergage of numbers: {avg:.2f}")
    print(f"Smallest number: {min_num}")
    print(f"Largest number: {max_num}")

def main():
    lower = 1
    upper = 100
    number_integers = get_input()
    random_list = generate_list(lower, upper, number_integers)
    do_thing(random_list)

main()