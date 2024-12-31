def read_file(file_name):
    file = open(file_name, "r")
    list = []
    for line in file:
        list.extend(int(line.strip().split()))
    return list

def main():
    file_name = input("Enter file:")
    list = read_file(file_name)
    print("Data from the entered file: ", list)
    print("The dorted Data: ", list.sort(reverse=True))

main()