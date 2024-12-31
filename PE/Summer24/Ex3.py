import sqlite3
import csv

def create_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            EmployeeID  TEXT PRIMARY KEY,
            EmployeeName TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            ProjectID  TEXT PRIMARY KEY,
            ProjectName TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee_projects (
        EmployeeID  TEXT,
        ProjectID TEXT,
        FOREIGN KEY (EmployeeID) REFERENCES employees(EmployeeID),
        FOREIGN KEY (ProjectID) REFERENCES projects(ProjectID),
        PRIMARY KEY (EmployeeID, ProjectID)                          
        );
    ''')

def insert_data(cursor):
    file = open("C:\\Users\\duong\\OneDrive\\Máy tính\\python\\PE\\Summer24-1\\employees.csv", "r")
    reader = csv.DictReader(file)
    next(reader, None)
    for row in reader:
        if len(row) != 2 or not row:
            continue
        else:
            cursor.execute('''
                Insert OR IGNORE into employees (EmployeeID, EmployeeName)
                values (?, ?)             
            ''', (row['EmployeeID'], row['EmployeeName']))

    file = open("C:\\Users\\duong\\OneDrive\\Máy tính\\python\\PE\\Summer24-1\\projects.csv", "r")
    reader = csv.DictReader(file)
    next(reader, None)
    for row in reader:
        if len(row) != 2 or not row:
            continue
        else:
            cursor.execute('''
                Insert OR IGNORE into projects (ProjectID, ProjectName)
                values (?, ?)             
            ''', (row['ProjectID'], row['ProjectName']))

    file = open("C:\\Users\\duong\\OneDrive\\Máy tính\\python\\PE\\Summer24-1\\employee_projects.csv", "r")
    reader = csv.DictReader(file)
    next(reader, None)
    for row in reader:
        if len(row) != 2 or not row:
            continue
        else:
            cursor.execute('''
                Insert OR IGNORE into employee_projects (EmployeeID, ProjectID)
                values (?, ?)             
            ''', (row['EmployeeID'], row['ProjectID']))

def main():
    conn = sqlite3.connect('C:\\Users\\duong\\OneDrive\\Máy tính\\python\\PE\\Summer24-1\\company_projects.sqlite')
    cursor = conn.cursor()

    create_table(cursor)
    insert_data(cursor)
    conn.commit()
    name = input("Enter an employee's name to find their projects: ").strip()
    cursor.execute('''
        Select p.ProjectID, p.ProjectName
        From projects p
        join employee_projects ep on ep.ProjectID = p.ProjectID
        join employees e on e.EmployeeID = ep.EmployeeID  
        where EmployeeName = ?
    ''', (name,))
    results = cursor.fetchall()
    if not results:
        print("No projects found for the employee")
    else:
        print(f"Proojects assigned to {name}")
        for id, name in results:
            print(f"{id} - {name}")
    conn.close()
    
main()