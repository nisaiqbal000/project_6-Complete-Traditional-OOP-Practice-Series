class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name, employees=None):
        self.name = name
        self.employees = employees or []
    
    def add_employee(self, employee):
        self.employees.append(employee)

# Usage
emp1 = Employee("John")
emp2 = Employee("Jane")
dept = Department("HR")
dept.add_employee(emp1)
dept.add_employee(emp2)

# Employees exist independently of department
print(emp1.name)  # John