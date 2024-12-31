import random

def generate_random_floats():
    while True:
        try:
            num_floats = int(input("How many random floating-point numbers would you like to generate? "))
            if num_floats <= 0:
                print("Please enter a number greater than 0.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    while True:
        try:
            lower_bound = float(input("Enter the lower bound of the range: "))
            upper_bound = float(input("Enter the upper bound of the range: "))
            if lower_bound >= upper_bound:
                print("Invalid range. The lower bound must be less than the upper bound.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter valid floating-point numbers.")

    # Generate random floats within the range
    random_floats = [round(random.uniform(lower_bound, upper_bound), 2) for _ in range(num_floats)]
    print(f"Generated list of floating-point numbers:\n{random_floats}")

    # Calculate the average and minimum value
    average = round(sum(random_floats) / num_floats, 2)
    minimum = min(random_floats)
    print(f"Average of the numbers: {average}")
    print(f"Minimum value in the list: {minimum}")

# Run the program
generate_random_floats()
