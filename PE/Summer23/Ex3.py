import sqlite3

def read_file(filename):
    """
    This function reads the data from the file and returns a list of dictionaries.
    """
    data = []
    with open(filename, "r") as f:
        for line in f:
            # Assuming the file contains comma-separated values in the format:
            # CustomerName,Product,Quantity,Price
            fields = line.strip().split(",")
            data.append({
                "CustomerName": fields[0],
                "Product": fields[1],
                "Quantity": int(fields[2]),
                "Price": float(fields[3])
            })
    return data

def calculate_discount(product, quantity, price):
    """
    This function calculates the discount and returns the amount.
    """
    if product == "Desktop":
        discount = price * 0.05 * quantity  # Assuming discount applies per unit
    else:
        discount = 0
    return discount

def calculate_total(quantity, price, discount):
    """
    This function calculates the total and returns the amount.
    """
    total = quantity * price - discount
    return total

def print_bill_list(data):
    """
    Prints the list of bills in a custom table format.
    """
    filtered_data = [row for row in data if row["Total"] > 15000000]
    sorted_data = sorted(filtered_data, key=lambda x: x["Total"], reverse=True)
    
    # Header
    print(f"{'Customer Name':<15} {'Product':<15} {'Quantity':<10} {'Price':<15} {'Money':<15} {'Discount':<15} {'Total':<15}")
    
    # Rows
    for row in sorted_data:
        print(f"{row['CustomerName']:<15} {row['Product']:<15} {row['Quantity']:<10} {row['Price']:<15,.2f} {row['Quantity'] * row['Price']:<15,.2f} {row['Discount']:<15,.2f} {row['Total']:<15,.2f}")


def save_to_database(data):
    """
    This function saves the data to the database.
    """
    connection = sqlite3.connect("C:\\Users\\duong\\OneDrive\\Máy tính\\python\\PE\\Summer23\\Bill.sqlite")
    cursor = connection.cursor()
    sql = """
    CREATE TABLE IF NOT EXISTS Bill (
        CustomerName TEXT,
        Product TEXT,
        Quantity INTEGER,
        Price REAL,
        Discount REAL,
        Total REAL
    )
    """
    cursor.execute(sql)
    for row in data:
        sql = "INSERT INTO Bill VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, (row["CustomerName"], row["Product"], row["Quantity"], row["Price"], row["Discount"], row["Total"]))
    connection.commit()
    connection.close()

def main():
    """
    This function reads the data from the file, calculates the discount and total,
    and saves the data to the database.
    """
    data = read_file("C:\\Users\\duong\\OneDrive\\Máy tính\\python\\PE\\Summer23\\Database.txt")
    for row in data:
        row["Discount"] = calculate_discount(row["Product"], row["Quantity"], row["Price"])
        row["Total"] = calculate_total(row["Quantity"], row["Price"], row["Discount"])
    
    print("Bills with Total > 15000000:")
    print_bill_list(data)
    save_to_database(data)

if __name__ == "__main__":
    main()
