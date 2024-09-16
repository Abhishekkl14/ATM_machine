#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class ATMMachine:
    def __init__(self):
        """
        Initializes the ATM machine with a default balance and no PIN.
        """
        self.__balance = 0.0  # Initial account balance in INR
        self.__pin = None  # User's PIN
        self.__transaction_history = []  # Log of transactions

    def set_pin(self, pin):
        """
        Sets the user's PIN.
        
        Args:
        pin (int): The user's PIN.
        """
        self.__pin = pin
        self.__transaction_history.append("PIN set successfully.")

    def check_pin(self, pin):
        """
        Verifies if the entered PIN is correct.
        
        Args:
        pin (int): The PIN to be verified.
        
        Returns:
        bool: True if the PIN is correct, False otherwise.
        """
        return self.__pin == pin

    def get_balance(self):
        """
        Returns the current balance of the user in INR.
        
        Returns:
        float: The current balance.
        """
        return self.__balance

    def withdraw_cash(self, amount):
        """
        Withdraws cash from the account if there is sufficient balance.
        
        Args:
        amount (float): The amount to be withdrawn in INR.
        
        Returns:
        str: The result of the withdrawal operation.
        """
        if amount > self.__balance:
            return "Insufficient balance."
        elif amount <= 0:
            return "Invalid withdrawal amount."
        else:
            self.__balance -= amount
            self.__transaction_history.append(f"Withdrew: ₹{amount:.2f}")
            return f"Withdrawal successful. Current balance: ₹{self.__balance:.2f}"

    def deposit_cash(self, amount):
        """
        Deposits cash to the account.
        
        Args:
        amount (float): The amount to be deposited in INR.
        
        Returns:
        str: The result of the deposit operation.
        """
        if amount <= 0:
            return "Invalid deposit amount."
        else:
            self.__balance += amount
            self.__transaction_history.append(f"Deposited: ₹{amount:.2f}")
            return f"Deposit successful. Current balance: ₹{self.__balance:.2f}"

    def change_pin(self, old_pin, new_pin):
        """
        Changes the user's PIN if the old PIN is correct.
        
        Args:
        old_pin (int): The user's current PIN.
        new_pin (int): The new PIN.
        
        Returns:
        str: The result of the PIN change operation.
        """
        if self.check_pin(old_pin):
            self.__pin = new_pin
            self.__transaction_history.append("PIN changed successfully.")
            return "PIN changed successfully."
        else:
            return "Incorrect old PIN."

    def view_transaction_history(self):
        """
        Returns the list of transactions made by the user.
        
        Returns:
        str: The transaction history.
        """
        if self.__transaction_history:
            return "\n".join(self.__transaction_history)
        else:
            return "No transactions yet."


def main():
    atm = ATMMachine()

    # Set PIN
    while True:
        pin = int(input("Set your PIN: "))
        confirm_pin = int(input("Confirm your PIN: "))
        if pin == confirm_pin:
            atm.set_pin(pin)
            print("PIN set successfully.")
            break
        else:
            print("PIN mismatch. Please try again.")

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Cash")
        print("3. Withdraw Cash")
        print("4. Change PIN")
        print("5. View Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Balance:", atm.get_balance())
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            print(atm.deposit_cash(amount))
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            print(atm.withdraw_cash(amount))
        elif choice == "4":
            old_pin = int(input("Enter old PIN: "))
            new_pin = int(input("Enter new PIN: "))
            print(atm.change_pin(old_pin, new_pin))
        elif choice == "5":
            print("Transaction History:\n", atm.view_transaction_history())
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




