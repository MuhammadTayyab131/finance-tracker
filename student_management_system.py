# import psycopg2

# class StudentManagementSystem:
#     def __init__(self):
#         try:
#             self.conn = psycopg2.connect(
#                 dbname = "studentdb",
#                 user = "postgress",
#                 password = "mian0909",
#                 host = "localhost",
#                 port = "5432"
#             )
#             self.cursor = self.conn.cursor()
#             self.create_table()
#         except Exception as e:
#             print("Database Connection Failed:", e)
#             exit()

#     def create_table(self):
#         self.cursor.execute("""
#             CREATE TABLE IF NOT EXISTS students(
#             roll_no INTEGER PRIMARY KEY,
#             name TEXT NOT NULL,
#             marks REAL NOT NULL
#             )
#         """)
#         self.conn.commit()

#     def calculate_grade(self,marks):
#         if marks >= 85:
#             return "A"
#         elif marks >= 70:
#             return "B"
#         elif marks >= 55:
#             return "C"
#         elif marks >= 40:
#             return "D"
#         else:
#             return "F"

#     def add_student(self):
#         try:
#             roll_no = int(input("\n\nEnter the roll_no: "))
#             name = input("Enter the name of student: ")
#             marks = float(input("Enter the marks of student: "))

#             self.cursor.execute(
#              "SELECT 1 FROM students WHERE roll_no=%s",
#               (roll_no,)
#             )
#             if self.cursor.fetchone():
#                 print("\n\nRoll_no already exists!")
#                 return
#             self.cursor.execute(
#                 "INSERT INTO students (roll_no, name, marks) VALUES (%s,%s,%s)",
#                 (roll_no, name, marks)
#             )
#             self.conn.commit()
#             print("Studend Successfully added!")
#         except ValueError:
#             print("\n\nInvalid input! Plaese enter correct value.")
#         except Exception as e:
#             print("Error Adding Student", e)
    
    
#     def view_student(self):
#         self.cursor.execute("SELECT * FROM students ORDER BY roll_no")
#         rows = self.cursor.fetchall()
#         if not rows:
#             print("No student Found")
#             return
#         print("-----list of all students-----")
#         for roll_no, name, marks in rows:
#             grade = self.calculate_grade(marks)
#             print(f"Roll_no {roll_no}, Name: {name}, Marks: {marks}, Grade: {grade}")


#     def search_student(self):
#             try:
#                 roll_no = int(input("\n\nEnter the roll_no to search the student: "))
#                 self.cursor.execute("SELECT * FROM students WHERE roll_no=%s",(roll_no))
#                 student = self.cursor.fetchone()

#                 if student:
#                     roll_no, name, marks = student
#                     grade = self.calculate_grade(marks)
#                     print(f"Name: {name}, marks: {marks}, Grade: {grade}")
#                 else:
#                     print("\n\nNo Student Found")    
#             except ValueError:
#                 print("\n\nInvalid input! Please enter correct value.")
#             except Exception as e:
#                 print("Error searching Student:", e)

#     def delete_student(self):
#         try:
#             roll_no = int(input("\n\nEnter the roll_no to search the student: "))
#             self.cursor.execute("DELETE * FROM students WHERE roll_no=%s",(roll_no))
#             if self.cursor.rowcount > 0:
#                 self.conn.commit()
#                 print("Student Deleted Successfully")

#             else:
#                 print("\n\nStudent not found")
#         except ValueError:
#             print("\n\nInvalid input! Please Enter the correct the value")
#         except Exception as e:
#             print("Error deleting Student", e)

#     def __del__(self):
#         if hasattr (self,'conn'):
#             self.cursor.close()
#             self.conn.close()

# # # main program
# sms = StudentManagementSystem()

# while True:
#     print("\n\n\n---------- Student Manegment System")
#     print("\n\n1. Add Student")
#     print("2. View Student")
#     print("3.Search Student")
#     print("4. Delete Student")
#     print("5.Exit")

#     choice = input("\n\nChose an Option from above: ")
     
#     if choice == "1":
#         sms.add_student()
#     elif choice == "2":
#         sms.view_student()
#     elif choice == "3":
#         sms.search_student()
#     elif choice == "4":
#         sms.delete_student()
#     elif choice == "5":
#         print("Exit Student Manegment System")
#         break
#     else:
#         print("\n\nInvalid choice Please try again")



import psycopg2

class StudentManagementSystem:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                dbname="studentdb",
                user="tayyab",
                password="mian0909",
                host="localhost",
                port="5432"
            )
            self.cursor = self.conn.cursor()
            self.create_table()
        except Exception as e:
            print("Database Connection Failed:", e)
            exit()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                roll_no INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                marks REAL NOT NULL
            )
        """)
        self.conn.commit()

    def calculate_grade(self, marks):
        if marks >= 85:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 55:
            return "C"
        elif marks >= 40:
            return "D"
        else:
            return "F"

    def add_student(self):
        try:
            roll_no = int(input("Enter roll no: "))
            name = input("Enter name: ")
            marks = float(input("Enter marks: "))

            self.cursor.execute(
                "SELECT 1 FROM students WHERE roll_no=%s",
                (roll_no,)
            )
            if self.cursor.fetchone():
                print("Roll number already exists!")
                return

            self.cursor.execute(
                "INSERT INTO students (roll_no, name, marks) VALUES (%s,%s,%s)",
                (roll_no, name, marks)
            )
            self.conn.commit()
            print("Student added successfully!")

        except ValueError:
            print("Invalid input!")
        except Exception as e:
            print("Error adding student:", e)

    def view_student(self):
        self.cursor.execute("SELECT * FROM students ORDER BY roll_no")
        rows = self.cursor.fetchall()

        if not rows:
            print("No students found")
            return

        print("\n--- Students List ---")
        for roll_no, name, marks in rows:
            grade = self.calculate_grade(marks)
            print(f"Roll_no: {roll_no}, Name: {name}, Marks: {marks}, Grade: {grade}")

    def search_student(self):
        try:
            roll_no = int(input("Enter roll no to search: "))
            self.cursor.execute(
                "SELECT * FROM students WHERE roll_no=%s",
                (roll_no,)
            )
            student = self.cursor.fetchone()

            if student:
                roll_no, name, marks = student
                grade = self.calculate_grade(marks)
                print(f"Name: {name}, Marks: {marks}, Grade: {grade}")
            else:
                print("Student not found")

        except ValueError:
            print("Invalid input!")
        except Exception as e:
            print("Error searching student:", e)

    def delete_student(self):
        try:
            roll_no = int(input("Enter roll no to delete: "))
            self.cursor.execute(
                "DELETE FROM students WHERE roll_no=%s",
                (roll_no,)
            )

            if self.cursor.rowcount > 0:
                self.conn.commit()
                print("Student deleted successfully")
            else:
                print("Student not found")

        except ValueError:
            print("Invalid input!")
        except Exception as e:
            print("Error deleting student:", e)

    def __del__(self):
        if hasattr(self, "conn"):
            self.cursor.close()
            self.conn.close()


# -------- Main Program --------
sms = StudentManagementSystem()

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        sms.add_student()
    elif choice == "2":
        sms.view_student()
    elif choice == "3":
        sms.search_student()
    elif choice == "4":
        sms.delete_student()
    elif choice == "5":
        print("Exiting system")
        break
    else:
        print("Invalid choice")
