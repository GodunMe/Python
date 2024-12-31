def sum_of_fractions(n):
    """
    This function takes an integer n and returns the sum of the fractions from 1 to n
    alternating between addition and subtraction, as well as the summation expression.
    """
    total = 1  # Starting with 1
    expression = "1"  # Start building the expression as a string
    for i in range(2, n + 1):
        if i % 2 == 0:
            total -= 1 / i
            expression += f" - 1/{i}"
        else:
            total += 1 / i
            expression += f" + 1/{i}"
    return expression, total

def main():
    """
    This function prompts the user for a number and prints out the sum of the fractions
    with the summation expression.
    """
    while True:
        try:
            n = int(input("Enter a positive integer number: "))
            if n <= 0:
                print("The number must be positive.")
            else:
                break
        except ValueError:
            pass
    
    expression, result = sum_of_fractions(n)
    print(f"Sum of fractions of {n}:\n{expression} = {result:.2f}")

if __name__ == "__main__":
    main()