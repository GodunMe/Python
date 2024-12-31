#Write a program to manage sholarship of student including student ID. Student name, class ID, class name and gpa.
#The program reads data from the file "sholarship.txt" and save to the database file sholarship.sqlite using the following table shemas.
#CLASS(ClassID, ClassName)
#STUDENT(SID, SName, ClassID, GPA)
#Note: Duplicates are not allowed in the Class table
#The program prints the excellent students including student name, class name, GPA and student whose GPA >= 8.5 and sorted in ascending order by by student name. Where scholar is fixed 500000.
#The output should be as follows:
#Excellent student:
#Student Name   Class   GPA Sholar

import sqlite3

#Read data from file and populate database
def populate_database():
    #Connect to the file SQLite database
    conn = sqlite3.connect("C:\\Users\\duong\\OneDrive\\Máy tính\\python\\PE\\Fall23\\Sholarship.sqlite")
    cursor = conn.cursor()

    #Create table
    cursor.execute("""
        Create table if not exists CLASS(
            ClassID text primary key,
            ClassName text
        )
    """)
    cursor.execute("""
        Create table if not exists STUDENT(
            SID text primary key,
            SName text Not Null,
            GPA real Not Null,
            ClassID text Not Null,
            Foreign key (ClassID) references CLASS(ClassID)
        )
    """)

    #Read data
    file = open("C:\\Users\\duong\\OneDrive\\Máy tính\\python\\PE\\Fall23\\sholarship.txt", "r")
    for line in file:
        sid, sname, classid, classname, gpa = line.strip().split(",")
        gpa = float(gpa)

        #Insert data to table CLASS
        cursor.execute("""
            Insert or ignore into CLASS(ClassID, ClassName)
            Values (?, ?)
        """, (classid, classname))

        #Insert data to table student
        cursor.execute("""
            Insert or ignore into STUDENT(SID, SName, ClassID, GPA)
            Values (?, ?, ?, ?)
        """, (sid, sname, classid, gpa))

    #Commit and close connect
    conn.commit()
    conn.close()

#Query excellent student
def print_excellent_students():
    #Connect to the file SQLite database
    conn = sqlite3.connect("C:\\Users\\duong\\OneDrive\\Máy tính\\python\\PE\\Fall23\\Sholarship.sqlite")
    cursor = conn.cursor()

    cursor.execute("""
        Select STUDENT.SName, CLASS.ClassName, STUDENT.GPA
        From STUDENT
        Join CLASS on STUDENT.ClassID = CLASS.ClassID
        Where GPA >= 8.5
        Order by SName asc
    """)
    results = cursor.fetchall()
    conn.close()

    print("Excellent student:")
    print(f"{'Student name': <15} {'Class': <10} {'GPA': <5} {'Scholar'}")
    for sname, classname, gpa in results:
        print(f"{sname:<15} {classname:<10} {gpa:<5} 500000")

def main():
    populate_database()
    print_excellent_students()

main()

# Thêm dữu liệu vào bảng
# INSERT INTO table_name (column1, column2, column3, ...)
# VALUES (value1, value2, value3, ...);

# Cập nhật dữ liệu
# UPDATE table_name
# SET column1 = value1, column2 = value2, ...
# WHERE condition;

# Xóa bảng
# DROP TABLE table_name;

# Xóa hàng
# DELETE FROM table_name
# WHERE condition;
