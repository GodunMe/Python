#The Fibonacci numbers are the numbers in the following integer sequence. 
#In mathematical items, the sequence Fn of Fibonacci numbers is defined by the recurrence relation.
#Fn = Fn-1 +Fn-2
#Write a program that repeatedly prompts a user for numbers until the user enters a positive integer number N. 
#Once a valid is entered, the program prints out the fibonacci sequence from 0 to N.
def generate_fibonacci(length):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) <= length:
        next_fibo = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibo)

    return fibonacci_sequence 
    
def get_input():
    while True:
        user_input = input("Enter a positive integer number: ")
        if user_input.isdigit() and int(user_input) > 0:
            n = int(user_input)  
            break  
    return n       

def main():
    length = get_input()
    fibonacci_sequence = generate_fibonacci(length)
    print(f"Fibonacci sequence 1 - {length}:")
    for i in range(len(fibonacci_sequence)):
        if i == len(fibonacci_sequence) - 1:
            print(fibonacci_sequence[i])
        else:
            print(fibonacci_sequence[i], end = ", ")
main()