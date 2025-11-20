# Create class Person (name, roll) and Marks (Maths, Computer). 
# Create class Student from Person and Marks. 
# Display student details and pass/fail, if 50% is needed for a pass.

class Person:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

class Marks:
    def __init__(self, maths, computer):
        self.maths = maths
        self.computer = computer

class Student(Person, Marks):
    def __init__(self, name, roll, maths, computer):
        Person.__init__(self, name, roll)
        Marks.__init__(self, maths, computer)

    def display(self):
        total = self.maths + self.computer
        percentage = total / 2  
        print(f"Name: {self.name}")
        print(f"Roll: {self.roll}")
        print(f"Maths: {self.maths}")
        print(f"Computer: {self.computer}")
        print(f"Percentage: {percentage}%")
        if percentage >= 50:
            print("Result: Pass")
        else:
            print("Result: Fail")

name = input("Enter name: ")
roll = input("Enter roll number: ")
maths = float(input("Enter Maths marks: "))
computer = float(input("Enter Computer marks: "))

student = Student(name, roll, maths, computer)
student.display()
