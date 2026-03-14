#Employee class inherited by Manager class

class Employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.salary = 0.0
        self.address = ""

    def get_input(self):
        self.name    = input("  Name    : ")
        self.age     = int(input("  Age     : "))
        self.salary  = float(input("  Salary  : "))
        self.address = input("  Address : ")

    def display(self):
        print(f"  Name    : {self.name}")
        print(f"  Age     : {self.age}")
        print(f"  Salary  : {self.salary:.2f}")
        print(f"  Address : {self.address}")


class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.department = ""

    def get_input(self):
        super().get_input()
        self.department = input("  Department: ")

    def display(self):
        super().display()
        print(f"  Department: {self.department}")


managers = []

print("=== Enter details for 10 Managers ===\n")
for i in range(10):
    print(f"Manager {i + 1}:")
    m = Manager()
    m.get_input()
    managers.append(m)
    print()

print("\n=== Manager Information ===\n")
for i, m in enumerate(managers):
    print(f"Manager {i + 1}:")
    m.display()
    print()