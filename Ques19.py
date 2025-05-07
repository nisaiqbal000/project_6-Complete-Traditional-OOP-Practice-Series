class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

# Usage
double = Multiplier(2)
print(callable(double))  # True
print(double(5))        # 10