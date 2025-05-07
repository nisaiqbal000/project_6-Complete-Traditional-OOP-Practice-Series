class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} car started")

# Usage
my_car = Car("Toyota")
print(my_car.brand)  # Access public variable
my_car.start()       # Call public method