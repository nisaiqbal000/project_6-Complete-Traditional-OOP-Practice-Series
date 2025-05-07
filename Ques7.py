class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name       # Public
        self._salary = salary  # Protected
        self.__ssn = ssn       # Private

# Usage
e = Employee("John", 50000, "123-45-6789")
print(e.name)      # Works
print(e._salary)   # Works but convention says "don't do this"
# print(e.__ssn)   # Will raise AttributeError
print(e._Employee__ssn)  # Name mangling allows access (but shouldn't be done)