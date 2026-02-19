import json
import hashlib
from datetime import datetime

DATA_FILE = "portal_data.json"
LOG_FILE = "activity.log"
ADMIN_FILE = "admin.json"


# ---------------- LOGGING ---------------- #

def log_activity(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.now()}] {msg}\n")


# ---------------- SECURITY ---------------- #

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def setup_admin():
    try:
        with open(ADMIN_FILE):
            return
    except FileNotFoundError:
        pwd = input("Create admin password: ")
        with open(ADMIN_FILE, "w") as f:
            json.dump({"password": hash_password(pwd)}, f)


def admin_login():
    with open(ADMIN_FILE) as f:
        data = json.load(f)

    for _ in range(3):
        pwd = input("Admin password: ")
        if hash_password(pwd) == data["password"]:
            log_activity("Admin logged in")
            return True
        print("❌ Wrong password")

    return False


# ---------------- CLASSES ---------------- #

class Student:
    def __init__(self, sid, name, email):
        self.id = sid
        self.name = name
        self.email = email
        self.__enrolled_courses = []
        self.__attendance = {}
        self.__marks = {}

    @property
    def enrolled_courses(self):
        return self.__enrolled_courses

    def enroll(self, course_code):
        if course_code not in self.__enrolled_courses:
            self.__enrolled_courses.append(course_code)
            self.__attendance[course_code] = 0
            self.__marks[course_code] = ()
            log_activity(f"Student {self.id} enrolled in {course_code}")

    def mark_attendance(self, course, percent):
        self.__attendance[course] = percent

    def assign_marks(self, course, marks_tuple):
        self.__marks[course] = marks_tuple

    def calculate_gpa(self):
        if not self.__marks:
            return 0

        total = 0
        count = 0

        for m in self.__marks.values():
            if m:
                avg = sum(m) / len(m)
                total += avg
                count += 1

        return round((total / count) / 20, 2) if count else 0

    def report(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "gpa": self.calculate_gpa()
        }

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "enrolled": self.__enrolled_courses,
            "attendance": self.__attendance,
            "marks": self.__marks
        }

    @staticmethod
    def from_dict(d):
        s = Student(d["id"], d["name"], d["email"])
        s.__enrolled_courses = d["enrolled"]
        s.__attendance = d["attendance"]
        s.__marks = {k: tuple(v) for k, v in d["marks"].items()}
        return s


class Teacher:
    def __init__(self, tid, name):
        self.id = tid
        self.name = name
        self.courses_teaching = set()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "courses": list(self.courses_teaching)
        }

    @staticmethod
    def from_dict(d):
        t = Teacher(d["id"], d["name"])
        t.courses_teaching = set(d["courses"])
        return t


class Course:
    def __init__(self, code, title, credits, teacher_id):
        self.code = code
        self.title = title
        self.credit_hours = credits
        self.teacher_id = teacher_id

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(d):
        return Course(**d)


# ---------------- PORTAL ---------------- #

class Portal:

    def __init__(self):
        self.students = {}
        self.teachers = {}
        self.courses = {}

    # ---------- ADD ---------- #

    def add_student(self):
        sid = input("ID: ")
        name = input("Name: ")
        email = input("Email: ")

        self.students[sid] = Student(sid, name, email)
        log_activity(f"Added student {sid}")

    def add_teacher(self):
        tid = input("ID: ")
        name = input("Name: ")

        self.teachers[tid] = Teacher(tid, name)
        log_activity(f"Added teacher {tid}")

    def add_course(self):
        code = input("Course code: ")
        title = input("Title: ")
        credits = int(input("Credits: "))
        tid = input("Teacher ID: ")

        if tid not in self.teachers:
            print("Teacher not found")
            return

        self.courses[code] = Course(code, title, credits, tid)
        self.teachers[tid].courses_teaching.add(code)

        log_activity(f"Added course {code}")

    # ---------- OPERATIONS ---------- #

    def enroll_student(self):
        sid = input("Student ID: ")
        code = input("Course code: ")

        self.students[sid].enroll(code)

    def mark_attendance(self):
        sid = input("Student ID: ")
        code = input("Course: ")
        p = float(input("Attendance %: "))
        self.students[sid].mark_attendance(code, p)

    def assign_marks(self):
        sid = input("Student ID: ")
        code = input("Course: ")

        marks = tuple(
            float(input(f"Mark {i+1}: ")) for i in range(3)
        )

        self.students[sid].assign_marks(code, marks)

    def calculate_gpa(self):
        for s in self.students.values():
            print(s.report())

    def search_records(self):
        name = input("Search name: ").lower()

        for s in self.students.values():
            if name in s.name.lower():
                print(s.report())

    # ---------- FILE ---------- #

    def save(self):
        data = {
            "students": {k: v.to_dict() for k, v in self.students.items()},
            "teachers": {k: v.to_dict() for k, v in self.teachers.items()},
            "courses": {k: v.to_dict() for k, v in self.courses.items()}
        }

        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)

        log_activity("Saved data")

    def load(self):
        try:
            with open(DATA_FILE) as f:
                data = json.load(f)

            self.students = {
                k: Student.from_dict(v)
                for k, v in data["students"].items()
            }

            self.teachers = {
                k: Teacher.from_dict(v)
                for k, v in data["teachers"].items()
            }

            self.courses = {
                k: Course.from_dict(v)
                for k, v in data["courses"].items()
            }

            print("✔ Data loaded")

        except FileNotFoundError:
            print("No saved file found")

    # ---------- SORT ---------- #

    def sort_by_gpa(self):
        ordered = sorted(
            self.students.values(),
            key=lambda s: s.calculate_gpa(),
            reverse=True
        )

        for s in ordered:
            print(s.report())


# ---------------- MAIN ---------------- #

def main():

    setup_admin()

    if not admin_login():
        return

    portal = Portal()
    portal.load()

    while True:

        print("""
1 Add student
2 Add teacher
3 Add course
4 Enroll student
5 Mark attendance
6 Assign marks
7 Calculate GPA
8 Search records
9 Save
10 Load
11 Sort by GPA
0 Exit
""")

        try:
            ch = int(input("Choice: "))

            if ch == 1:
                portal.add_student()
            elif ch == 2:
                portal.add_teacher()
            elif ch == 3:
                portal.add_course()
            elif ch == 4:
                portal.enroll_student()
            elif ch == 5:
                portal.mark_attendance()
            elif ch == 6:
                portal.assign_marks()
            elif ch == 7:
                portal.calculate_gpa()
            elif ch == 8:
                portal.search_records()
            elif ch == 9:
                portal.save()
            elif ch == 10:
                portal.load()
            elif ch == 11:
                portal.sort_by_gpa()
            elif ch == 0:
                portal.save()
                print("Goodbye 👋")
                break

        except Exception as e:
            print("❌ Error:", e)


if __name__ == "__main__":
    main()

