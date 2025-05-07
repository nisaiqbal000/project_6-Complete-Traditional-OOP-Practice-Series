class Bank:
    bank_name = "Default Bank"
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Usage
b1 = Bank()
print(b1.bank_name)  # Default Bank

Bank.change_bank_name("New Bank")
b2 = Bank()
print(b1.bank_name)  # New Bank (existing instance affected)
print(b2.bank_name)  # New Bank