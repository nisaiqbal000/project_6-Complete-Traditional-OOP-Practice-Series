# Complete Traditional OOP Practice Series

## 1. Using `self`
**Steps:**
- Create a class `Student`
- Define `__init__` method with `self`, `name`, and `marks` parameters
- Assign parameters to instance variables using `self`
- Create `display` method that prints the details

## 2. Using `cls`
**Steps:**
- Create class `Counter` with class variable `count = 0`
- Define `__init__` method that increments `count`
- Create class method `get_count` using `@classmethod` decorator
- Return `cls.count` in the class method

## 3. Public Variables and Methods
**Steps:**
- Create class `Car`
- Define public variable `brand` in `__init__`
- Create public method `start()`
- Instantiate and access both

## 4. Class Variables and Class Methods
**Steps:**
- Create class `Bank` with class variable `bank_name`
- Add class method `change_bank_name` using `@classmethod`
- Modify `bank_name` using `cls`
- Show effect on instances

## 5. Static Variables and Static Methods
**Steps:**
- Create class `MathUtils`
- Add static method `add` using `@staticmethod`
- Return sum of parameters
- Call without instantiating

## 6. Constructors and Destructors
**Steps:**
- Create class `Logger`
- Define `__init__` for constructor
- Define `__del__` for destructor
- Add print statements in both

## 7. Access Modifiers
**Steps:**
- Create class `Employee`
- Add public, protected, and private variables
- Try accessing them from outside
- Document behavior

## 8. The `super()` Function
**Steps:**
- Create base class `Person` with name
- Create derived class `Teacher`
- Use `super()` in `Teacher.__init__`
- Add subject attribute

## 9. Abstract Classes and Methods
**Steps:**
- Import `ABC` and `abstractmethod`
- Create abstract class `Shape`
- Define abstract method `area()`
- Create concrete class `Rectangle`

## 10. Instance Methods
**Steps:**
- Create class `Dog`
- Add instance variables in `__init__`
- Create instance method `bark()`
- Use instance variables in method

## 11. Class Methods
**Steps:**
- Create class `Book` with class variable
- Add class method to increment count
- Call class method in `__init__`

## 12. Static Methods
**Steps:**
- Create class `TemperatureConverter`
- Add static method for conversion
- Call without instance

## 13. Composition
**Steps:**
- Create `Engine` class with method
- Create `Car` class that takes `Engine` in `__init__`
- Access engine method through car

## 14. Aggregation
**Steps:**
- Create `Employee` class
- Create `Department` class that can hold employees
- Show independent existence

## 15. MRO and Diamond Inheritance
**Steps:**
- Create class hierarchy A -> B, A -> C, B & C -> D
- Override `show()` in each
- Call on D instance
- Check MRO

## 16. Function Decorators
**Steps:**
- Create decorator function
- Add wrapper that prints message
- Apply to target function

## 17. Class Decorators
**Steps:**
- Create decorator function that modifies class
- Add new method to class
- Return modified class
- Apply to target class

## 18. Property Decorators
**Steps:**
- Create class with private `_price`
- Add `@property` for getter
- Add `@price.setter` for setter
- Add `@price.deleter` for deleter

## 19. `callable()` and `__call__()`
**Steps:**
- Create class with `__init__` to set factor
- Define `__call__` method
- Test with `callable()`
- Call instance like function

## 20. Custom Exception
**Steps:**
- Define custom exception class
- Create function that raises it
- Use try-except to handle

## 21. Custom Iterable Class
**Steps:**
- Create class with `__init__` to set start
- Implement `__iter__` to return self
- Implement `__next__` for countdown logic
- Raise `StopIteration` at end

This completes all 21 OOP practice assignments. Each example demonstrates a key OOP concept in Python with practical implementation.
