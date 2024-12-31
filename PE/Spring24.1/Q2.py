from collections import Counter

# Helper function to check if a number is perfect
def is_perfect_number(n):
    if n <= 0:
        return False
    divisors = [i for i in range(1, n//2+1) if n % i == 0]
    return sum(divisors) == n

def main():
    # Read numbers from the file
    try:
        with open("data_1.txt", "r") as file:
            content = file.read()
            numbers = [int(num) for num in content.split(",")]
    except FileNotFoundError:
        print("Error: The file 'data_1.txt' does not exist.")
        return
    except ValueError:
        print("Error: The file contains invalid data.")
        return

    # Identify perfect numbers
    perfect_numbers = [num for num in numbers if is_perfect_number(num)]
    print(f"Perfect numbers from the file: {perfect_numbers}")

    # Count occurrences of each perfect number
    occurrences = Counter(perfect_numbers)
    print(f"Occurrences of each perfect number: {dict(occurrences)}")

    # Find the number(s) with the highest frequency
    max_frequency = max(occurrences.values(), default=0)
    most_frequent_numbers = [num for num, count in occurrences.items() if count == max_frequency]
    print(f"Number(s) with the highest frequency: {', '.join(map(str, most_frequent_numbers))}")


# Run the program
main()
