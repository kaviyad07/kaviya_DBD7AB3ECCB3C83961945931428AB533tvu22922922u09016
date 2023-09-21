'''Implement a class called BankAccount that represents a                bank account. the class should have private 
attributes for account number, account holder name, and               account balance. Include methods to
deposit money, withdraw money, and display the account               balance. Ensure that the account balance 
cannot be accessed directly from outside the class. Write a          program to create an instance of the
BankAccount class and test the deposit and withdrawal      functionality.'''


class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self._account_balance}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._account_balance}")
        elif amount > self._account_balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Please enter a positive amount.")

    def display_balance(self):
        print(f"Account balance for {self._account_holder_name}: ${self._account_balance}")

# Testing the BankAccount class
if __name__ == "__main__":
    # Creating an instance of BankAccount
    account = BankAccount("12345", "Kaviya", 1000)

    # Testing deposit and withdrawal
    account.display_balance()
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(1500)
    account.display_balance()


                                                  
