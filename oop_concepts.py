class Developer:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def show_details(self):
        print(f"Developer Name: {self.name}")
        print(f"Role: {self.role}")
class AIDeveloper(Developer):
    def __init__(self, name, role, primary_language):
        super().__init__(name, role)
        self.primary_language = primary_language
    def show_details(self):
        super().show_details()
        print(f"Primary Language: {self.primary_language}\n")

def main():
    print("--- Object-Oriented Programming ---")
    dev1 = Developer("Amit", "Backend Developer")
    dev2 = AIDeveloper("Rahul", "Machine Learning Engineer", "Python")

    dev1.show_details()
    print("-" * 20)
    dev2.show_details()

if __name__ == "__main__":
    main()