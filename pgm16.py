# Compare above 2 students based on pass percentage.
# Base class 1: Person
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

    def percentage(self):
        return (self.maths + self.computer) / 2

    def display(self):
        pct = self.percentage()
        print(f"Name: {self.name}")
        print(f"Roll: {self.roll}")
        print(f"Maths: {self.maths}")
        print(f"Computer: {self.computer}")
        print(f"Percentage: {pct}%")
        print("Result: Pass" if pct >= 50 else "Result: Fail")

print("Enter details for Student 1:")
name1 = input("Name: ")
roll1 = input("Roll: ")
maths1 = float(input("Maths marks: "))
computer1 = float(input("Computer marks: "))
student1 = Student(name1, roll1, maths1, computer1)

print("\nEnter details for Student 2:")
name2 = input("Name: ")
roll2 = input("Roll: ")
maths2 = float(input("Maths marks: "))
computer2 = float(input("Computer marks: "))
student2 = Student(name2, roll2, maths2, computer2)

print("\nStudent 1 Details:")
student1.display()
print("\nStudent 2 Details:")
student2.display()

pct1 = student1.percentage()
pct2 = student2.percentage()

print("\nComparison Result:")
if pct1 > pct2:
    print(f"{student1.name} has a higher percentage ({pct1}%) than {student2.name} ({pct2}%)")
elif pct2 > pct1:
    print(f"{student2.name} has a higher percentage ({pct2}%) than {student1.name} ({pct1}%)")
else:
    print(f"Both students have the same percentage ({pct1}%)")
