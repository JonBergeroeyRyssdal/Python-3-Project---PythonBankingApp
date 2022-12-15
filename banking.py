class Bank:

    def __init__(self):
        with open('account.py', 'r') as file:
            self.balance = (file.read())
           
    def withdrawal(self):
        try:
            amount = input("\nHow much would you like to withdraw? ")
            amount = float(amount)
            assert amount > 0
        except ValueError or AssertionError:
            amount = 0

        self.balance = float(self.balance)

        self.balance = self.balance - amount

        if self.balance < float(0):
            self.balance = self.balance + amount
            print("You don't have this funds in your account.")
            
        else:
            with open('account.py', 'w') as file:
                file.write(f"{self.balance}")
            print(f"\nYou withdrew: {amount}")

    def deposit(self):
        try:
            amount = input("\nHow much would you like to deposit? ")
            amount = float(amount)
            assert amount > 0
        except ValueError or AssertionError:
            amount = 0
        self.balance = float(self.balance)
        self.balance = self.balance + amount
        with open('account.py', 'w') as file:
            file.write(f"{self.balance}")
        print(f"\nYou deposited: {amount}")

    def checking_balance(self):
        with open('account.py', 'r') as file:
            self.balance = (file.read())
        print(f"\nYou're balance is: {self.balance}")

banking = Bank()

in_use = True

while in_use:

    user = input("\nDo you want to: \n\nWithdrawal (w) \nDeposit (d) \nCheck balance (b) \nExit the bank (e/q)? ").lower()

    if user == "w":
        banking.withdrawal()
        banking.checking_balance()
        

        new_action = True

        while new_action:

            other_action = input("\nDo you want to do another action? ('y'/'n') ").lower()

            if other_action == "y":
                in_use = True
                new_action = False

            elif other_action == "n":
                print("\nThanks for using this bank. Welcome back.")
                in_use = False
                new_action = False

            else: 
                new_action = True

    elif user == "d":
        banking.deposit()
        banking.checking_balance()

        new_action = True

        while new_action:

            other_action = input("\nDo you want to do another action? ('y'/'n') ").lower()

            if other_action == "y":
                in_use = True
                new_action = False

            elif other_action == "n":
                print("\nThanks for using this bank. Welcome back.")
                in_use = False
                new_action = False

            else: 
                new_action = True

    elif user == "b":
        banking.checking_balance()

        new_action = True

        while new_action:

            other_action = input("\nDo you want to do another action? ('y'/'n') ").lower()

            if other_action == "y":
                in_use = True
                new_action = False

            elif other_action == "n":
                print("\nThanks for using this bank. Welcome back.")
                in_use = False
                new_action = False

            else: 
                new_action = True


    elif user in ["e", "q"]:
        print("\nThanks for using this bank. Welcome back.")
        in_use = False
    
    else:
        True

    


    
    


