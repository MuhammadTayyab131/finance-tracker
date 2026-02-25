
import json
import os

class Account:
    def __init__(self,name,pin):
        self.name = name
        self.pin = pin
        self.balance = 0
        self.transaction_history = []
        self.load_data()

    def category(self):
        category = input("enter categoery: (e.g Food, transport, salary)").strip()
        if category == "":
            category = "others"
        return category

    def deposit(self,amount):
        category = self.category()
        if amount <= 0 :
            print("deposit amount should be greater then 0")
            return
        self.balance += amount
        self.transaction_history.append({
            "type": "deposit",
            "amount": amount,
            "category": category
        })
        self.save_data()
        print("amount deposited successfully")
    
    
    
    def withdraw(self,amount):
        category = self.category()
        if amount <= 0:
            print("please enter the amount greater then 0")
            return
        if amount > self.balance:
            print("please enter the amount in the range of balance")
            return
        self.balance -= amount
        self.transaction_history.append({
            "type": "withdraw",
            "amount": amount,
            "category": category
        })
        self.save_data()
        print("amount withdraw successfully")

    def check_balance(self):
        print(f"Your current balance is: {self.balance}")
    
    def history(self):
        if not self.transaction_history:
            print("No transation yet")
            return
        for j,i in enumerate(self.transaction_history, start=1):
            print(f"{j}. {i['type']} -- {i['amount']} category: {i['category']}")
    

    def save_data(self):
        data = {
            "pin": self.pin,
            "balance": self.balance,
            "history": self.transaction_history
        }
        with open(f"{self.name}.json", "w") as f:
            json.dump(data, f)

    def load_data(self):
        try:
            with open(f"{self.name}.json", "r") as f:
                data = json.load(f)
                self.pin = data["pin"]
                self.balance = data["balance"]
                self.transaction_history = data["history"]
        except FileNotFoundError:
            pass

    ################## bank saystem ###############

class Bank_system:
    def __init__(self):
        self.user = {}
        self.load_accounts()
    
    def create_account(self,name,pin):
        if name in self.user :
            print("user already exsits")
        else:
            self.user[name] = Account(name,pin)
            print("Account created successfully")
    
    def login_account(self,name,pin):
        if name in self.user and self.user[name].pin == pin:
            return self.user[name]
        else:
            print("Invalid name or pin")
            return None

    def load_accounts(self):
        files = os.listdir()

        for file in files:
            if file.endswith(".json"):
                try:
                    with open(file, "r") as f:
                        data = json.load(f)
                    if "pin" in data and "balance" in data:
                        username = file.replace(".json", "")
                        account = Account(username, "")
                        self.user[username] = account
                except:
                    pass


    def banking_menu(self,account):
        while True:
            print("1.deposit amount")
            print("2.withdraw amount")
            print("3.check balance")
            print("4.transation history")
            print("5.back")

            choice = input("Select any above option: ")

            if choice == "1":
                amount = float(input("Enter the deposit amount: "))
                account.deposit(amount)
            
            elif choice == "2":
                amount = float(input("Entetr the withdraw amount: "))
                account.withdraw(amount)

            elif choice == "3":
                account.check_balance()
            
            elif choice == "4":
                account.history()
            
            elif choice == "5":
                break

            else:
                print("Invalid entery")

    # # save data
    # def save_data(self):
    #     with open("transaction_history.json", "w") as f:
    #         json.dump(self.transaction_history,f)

    # # load data
    # def load_data(self):
    #     try:
    #         with open("transaction_history.jeson", "r") as f:
    #             self.transaction_history = json.load(f)
    #     except FileNotFoundError:
    #         self.transaction_history = []


    def main_menu(self):
        while True:
            print("1.create account")
            print("2.select account")
            print("3.exit")

            choice = input("Enter any above option: ")

            if choice == "1":
                name = input("Enter the user Name: ")
                pin = input("Enter PIN: ")
                self.create_account(name,pin)
            elif choice == "2":
                name = input("Enter account name: ")
                pin = input("Enter PIN: ")
                account = self.login_account(name,pin)
                if account:
                    self.banking_menu(account)
            elif choice == "3":
                print("Thanks for using bank system")
                break
            else:
                print("Invalid choice")


bank = Bank_system()
bank.main_menu()