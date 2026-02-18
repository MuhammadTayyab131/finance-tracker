# # ===== STAGE 1 : BASIC STUDENT PORTAL =====

# class Student:
#     def __init__(self, s_id, name):
#         self.id = s_id
#         self.name = name
#         self.courses = {}

#     def enroll(self, code):
#         if code not in self.courses:
#             self.courses[code] = {}

#     def assign_marks(self, code):
#         mid = float(input("Enter Mid marks: "))
#         assign = float(input("Enter Assignment marks: "))
#         finals = float(input("Enter Final marks: "))

#         self.courses[code] = {
#             "Mids": mid,
#             "Assignment": assign,
#             "Finals": finals
#         }

#     def gpa(self):
#         if not self.courses:
#             return 0

#         total = 0
#         count = 0

#         for marks in self.courses.values():
#             if marks:
#                 weighted_avg = (
#                     marks["Mids"] * 0.3 +
#                     marks["Assignment"] * 0.1 +
#                     marks["Finals"] * 0.6
#                 )
#                 total += weighted_avg
#                 count += 1

#         return round((total / count) / 25, 2) if count else 0


# class Portal:
#     def __init__(self):
#         self.students = {}

#     def add_student(self):
#         s_id = input("Enter student ID: ")
#         name = input("Enter student name: ")
#         self.students[s_id] = Student(s_id, name)

#     def enrollment(self):
#         s_id = input("Enter student ID: ")
#         code = input("Enter course code: ")

#         if s_id in self.students:
#             self.students[s_id].enroll(code)
#         else:
#             print("Student ID not found!")

#     def assign_marks(self):
#         s_id = input("Enter student ID: ")
#         code = input("Enter course code: ")

#         if s_id in self.students and code in self.students[s_id].courses:
#             self.students[s_id].assign_marks(code)
#         else:
#             print("Student or Course not found!")

#     def show_marks(self):
#         print("\n--- Student GPA ---")
#         for s in self.students.values():
#             print(f"{s.id} | {s.name} GPA: {s.gpa()}")


# def main():
#     portal = Portal()

#     while True:
#         print("""
# 1 Add student
# 2 Enroll student
# 3 Assign marks
# 4 Show GPA
# 0 Exit
# """)

#         ch = int(input("Select option: "))

#         if ch == 1:
#             portal.add_student()
#         elif ch == 2:
#             portal.enrollment()
#         elif ch == 3:
#             portal.assign_marks()
#         elif ch == 4:
#             portal.show_marks()
#         elif ch == 0:
#             break
#         else:
#             print("Wrong input!")


# main()


# ==============================
# PYTHON OOP MASTER DEMO
# ==============================

from abc import ABC, abstractmethod

# ------------------------------------------------
# 1️⃣ BASIC CLASS & OBJECT
# ------------------------------------------------
class Person:
    species = "Human"        # Class Variable (shared)

    def __init__(self, name, age):
        self.name = name     # Instance Variable
        self.age = age

    def introduce(self):     # Instance Method
        return f"My name is {self.name} and I am {self.age} years old."


p1 = Person("Ali", 25)
p2 = Person("Ahmed", 30)

# ------------------------------------------------
# 2️⃣ CLASS METHOD & STATIC METHOD
# ------------------------------------------------
class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def info(cls):
        return f"This is {cls.__name__} class"


# ------------------------------------------------
# 3️⃣ ENCAPSULATION (PRIVATE VARIABLES)
# ------------------------------------------------
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


# ------------------------------------------------
# 4️⃣ INHERITANCE & SUPER()
# ------------------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # Call parent constructor
        self.breed = breed

    def speak(self):               # Method Overriding
        return "Bark"


# ------------------------------------------------
# 5️⃣ POLYMORPHISM (Duck Typing)
# ------------------------------------------------
class Cat:
    def speak(self):
        return "Meow"


def animal_sound(animal):
    print(animal.speak())


# ------------------------------------------------
# 6️⃣ ABSTRACTION (ABC)
# ------------------------------------------------
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


# ------------------------------------------------
# 7️⃣ MAGIC / DUNDER METHODS
# ------------------------------------------------
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.pages == other.pages


# ------------------------------------------------
# 8️⃣ COMPOSITION (HAS-A Relationship)
# ------------------------------------------------
class Engine:
    def start(self):
        return "Engine started"


class Car:
    def __init__(self):
        self.engine = Engine()   # Composition

    def drive(self):
        return self.engine.start() + " -> Car is moving"


# ------------------------------------------------
# 9️⃣ MULTIPLE INHERITANCE & MRO
# ------------------------------------------------
class A:
    def show(self):
        return "Class A"


class B:
    def show(self):
        return "Class B"


class C(A, B):
    pass


# ------------------------------------------------
# 🔟 TESTING EVERYTHING (MAIN)
# ------------------------------------------------
if __name__ == "__main__":

    # Basic
    print(p1.introduce())
    print(Person.species)

    # Static & Class methods
    print(MathUtils.add(5, 3))
    print(MathUtils.info())

    # Encapsulation
    account = BankAccount("Ali", 1000)
    account.deposit(500)
    print(account.get_balance())

    # Inheritance
    dog = Dog("Buddy", "Labrador")
    print(dog.name, dog.breed)
    print(dog.speak())

    # Polymorphism
    animal_sound(dog)
    animal_sound(Cat())

    # Abstraction
    square = Square(4)
    print("Square Area:", square.area())

    # Dunder methods
    b1 = Book("Python", 300)
    b2 = Book("Java", 300)
    print(str(b1))
    print("Pages:", len(b1))
    print("Books Equal:", b1 == b2)

    # Composition
    car = Car()
    print(car.drive())

    # MRO
    c = C()
    print(c.show())
    print(C.__mro__)
