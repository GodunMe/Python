#Write a program that reads a text file, extracts all even numbers, and save them to a new file.

def main():
    input_file_name = "C:\\Users\\duong\\OneDrive\\Máy tính\\python\\PE\\Summer24-1\\integers_data.txt"
    file = open(input_file_name, "r")
    num_list = file.read().split()
    even_num = [num for num in num_list if int(num) % 2 == 0]
    
    output_file_name = "C:\\Users\\duong\\OneDrive\\Máy tính\\python\\PE\\Summer24-1\\even_numbers.txt"
    even_file = open(output_file_name, "w")
    even_file.write(" ".join(even_num))

main()