# --- Object-Oriented Programming (OOP) ---

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course
        
    def introduce(self):
        return f"I'm {self.name}, enrolled in {self.course}"

s1 = Student("Priya", "Gen AI & ML")
print(s1.introduce())

class InternStudent(Student): # inherits from Student
    def introduce(self):
        return f"{self.name} is interning via Triadix OIP"

# Testing the inherited class
s2 = InternStudent("Rahul", "Gen AI & ML")
print(s2.introduce())