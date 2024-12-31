import sqlite3
import csv

def create_database():
    """Create and set up the library database."""
    connection = sqlite3.connect("C:\\Users\\duong\\OneDrive\\Máy tính\\python\\PE\\SP24-1\\library.sqlite")
    cursor = connection.cursor()
    
    # Create books table (no authors table)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT
        )
    """)
    connection.commit()
    return connection

def insert_data_from_csv(connection, csv_file):
    """Insert book data from CSV into the database."""
    cursor = connection.cursor()
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Insert book data directly (author is stored in books table)
            cursor.execute("""
                INSERT OR IGNORE INTO books (id, title, author) VALUES (?, ?, ?)
            """, (row["book id"], row["title"], row["author"]))
    connection.commit()

def find_books_by_author(connection, author_name):
    """Find and print books by the given author."""
    cursor = connection.cursor()
    cursor.execute("""
        SELECT title
        FROM books
        WHERE author = ?
    """, (author_name,))
    books = cursor.fetchall()
    if books:
        print(f"Books by {author_name}:")
        for book in books:
            print(book[0])
    else:
        print(f"No books found for the author: {author_name}")

def main():
    # Create the database and tables
    connection = create_database()

    # Insert data from CSV
    csv_file = "C:\\Users\\duong\\OneDrive\\Máy tính\\python\\PE\\SP24-1\\book_data.csv"
    insert_data_from_csv(connection, csv_file)

    # Prompt the user for an author's name
    author_name = input("Enter an author's name to find their books: ")
    find_books_by_author(connection, author_name)

    # Close the connection
    connection.close()

# Content of "book_data.csv":
# book id,title,author
# 1,The Great Gatsby,F. Scott Fitzgerald
# 2,To Kill a Mockingbird,Harper Lee
# 3,The Catcher in the Rye,J.D. Salinger
# 4,Go Set a Watchman,Harper Lee

if __name__ == "__main__":
    main()
