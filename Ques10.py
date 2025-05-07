class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} the {self.breed} says Woof!")

# Usage
d = Dog("Buddy", "Golden Retriever")
d.bark()  # Buddy the Golden Retriever says Woof!