# --- Python Basics ---
print("Hello, Triadix OIP")

# --- Variables & Data Types ---
name = "Rashmi"      # str
age = 24             # int
gpa = 8.7            # float
is_active = True     # bool
skills = ["Python", "SQL"] # list
profile = {"role": "Intern"} # dict

# --- Functions ---
def calculate_average(scores):
    return sum(scores) / len(scores)

result = calculate_average([85, 90, 78])
print(result) # 84.33

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Rashmi")
greet("Rashmi", greeting="Hi")

square = lambda x: x ** 2

# --- Loops & Conditional Statements ---
score = 78
if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
else:
    print("Needs Improvement")

students = ["Aman", "Priya", "Rahul"]
for student in students:
    print(f"Hello, {student}")

for i, student in enumerate(students):
    print(i, student)

# --- File Handling ---
with open("notes.txt", "w") as f:
    f.write("Week 1 complete")

with open("notes.txt", "r") as f:
    content = f.read()
    print(content)