class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older")
    print("Age is valid")

# Usage
try:
    check_age(15)
except InvalidAgeError as e:
    print(f"Error: {e}")  # Error: Age must be 18 or older