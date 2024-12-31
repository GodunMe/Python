#Write aprogram named read_file_and_find_primes that reads a text file named "data_1.txt".
#The program saves all prime numbers to a list, and then display the content of the file, 
#display the occurences od each number in list, and the number with the first highest frequency.

import math

def read_file_and_find_primes():
    file_name="C:\\Users\\duong\\OneDrive\\Máy tính\\python\\PE\\Spring24\\data_1.txt"
    file = open(file_name, "r")
    data_list = file.read().strip().split(",")
    prime_list = []
    for num in data_list:
        if is_prime(num):
            prime_list.append(num)
    return prime_list

def is_prime(number):
    number = int(number)
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    #isqrt = int sqrt
    for i in range(3, math.isqrt(number)+1, 2):
        if number % i == 0:
            return False
    return True
    
def process_data(prime_list):
    prime_dic = {}
    for num in prime_list:
        prime_dic[num] = prime_dic.get(num, 0) + 1
    most_frequency_num = max(prime_dic, key=prime_dic.get)
    most_frequency_count = prime_dic[most_frequency_num]
    print("Prime numbers from the file: [", ", ".join(prime_list), end = "]\n")
    print("Frequency of each number:")
    for num, count in prime_dic.items():
        print(f"Number {num}: {count} times")
    print(f"The number with the highest frequency: {most_frequency_num} (Frequency: {most_frequency_count})")

def main():
    prime_list = read_file_and_find_primes()
    process_data(prime_list)

main()