# Write a program that implement following tasks:
# Read student information from student data.csv file.
# Then insert the department and student data into these tables of database named university.sqlite. You must ensure not to duplicate department entries.
# Ask user enter a department name, the program will print a list of students belong to the department. Otherwise, print "No students found in the department".
# Content of the input file "student_data.csv":
# Student ID, StudentName, DepartmentName
# S1, John Doe, Computer Science
# S2, Jane Smith, Mathematics
# S3, Emily Johnson, Physics
# S4, Mike Brown, Computer Science
# S5, Laura Wilson, Mathematics
# S6, Chris Garcia, Engineering
# Result of the program:
# Enter a department name to find students: Computer Science
# Students in Computer Science:
# S1- John Doe
# S4- Mike Brown

import sqlite3
import csv

def create_table(cursor):
    cursor.execute("""
        Create table if not exists STUDENT(
            StudentID text primary key,
            StudentName text not null,
            DepartmentName text not null
        )
    """)

def insert_student(cursor, students):
    for student in students:
        cursor.execute("""
        Insert into STUDENT (StudentID, StudentName, DepartmentName)
        Values (?, ?, ?)
        """, (student['StudentID'], student['StudentName'], student['DepartmentName']))

def read_student_data():
    students = []
    file = open('C:\\Users\\duong\\OneDrive\\Máy tính\\python\\PE\\Fall23\\student_data.csv', "r")
    reader = csv.DictReader(file)
    for row in reader:
        students.append({
            'StudentID': row['Student ID'],
            'StudentName': row['StudentName'],
            'DepartmentName': row['DepartmentName'],
        })
    return students

def get_students_in_student(cursor, department_name):
    cursor.execute("""
        SELECT StudentID, StudentName 
        FROM Student
        WHERE DepartmentName = ?
    """, (department_name,))
    students = cursor.fetchall()
    return students

def main(): 
    conn = sqlite3.connect('C:\\Users\\duong\\OneDrive\\Máy tính\\python\\PE\\Fall23\\univerity.sqlite')
    cursor = conn.cursor()

    create_table(cursor)
    students = read_student_data()
    insert_student(cursor, students)

    department_name = input("Enter a department name to find student: ")
    st_in_dep = get_students_in_student(cursor, department_name)
    if st_in_dep:
        print(f"Students in {department_name}:")
        for StudentID, StudentName in st_in_dep:
            print(f"{StudentID}- {StudentName}")
    else:
        print("No students found in the department.")

main()