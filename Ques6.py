class Logger:
    def __init__(self):
        print("Logger object created")
    
    def __del__(self):
        print("Logger object destroyed")

# Usage
l = Logger()  # Prints "Logger object created"
del l         # Prints "Logger object destroyed"