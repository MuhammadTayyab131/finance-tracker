
class Finance_tracker:
    def __init__(self):
        self.transactions = []

    def get_amount(self):
        while True:
            amount = input("Enter amount: ")
            try:
                amount = float(amount)
                if amount <= 0:
                    print("Amount must be greater then zero!")
                else:
                    return amount
            except ValueError:
                print("please Enter a valid number.")

# category
    def get_category(self):
        category = input("Enter the category (e.g food, transport, salary): ").strip()
        if category == "":
            category = "others"
        return category
    


    #  income

    def add_income(self):
        amount = self.get_amount()
        category = self.get_category()
        self.transactions.append({
            "type": "income",
            "amount": amount,
            "category" : category
        })
        print("Encome added successfuly!")

# balance
    def get_balance(self):
            balance = 0
            for i in self.transactions:
                if i["type"] == "income":
                    balance += i["amount"]
                else:
                    balance -= i["amount"]
            return balance


    # expense
    def add_expense(self):
        amount = self.get_amount()
        balance = self.get_balance()
        category = self.get_category()
        if amount > balance:
            print("Expense exceeding current balance")
            return
        self.transactions.append({
            "type": "expense",
            "amount": amount ,
            "category": category
        })
        print("Expense added successfully")

# show balance

    def view_balance(self):
        balance = self.get_balance()
        print(f"Current Balance: {balance}")

    # transaction 

    def history(self):
        if not self.transactions:
            print("no transaction found yet")
            return
        for j,i in enumerate(self.transactions, start =1):
            print(f"{j} {i['type']} -> {i['amount']} category: {i['category']}")

    def show_menu(self):
        print("\n Personal Finance Tracker ")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Transaction History")
        print("5. Exit")
    def output(self):
        while True:
            self.show_menu()
            choice = input("choose an option: ")

            if choice == "1":
                self.add_income()
            elif choice == "2":
                self.add_expense()
            elif choice =="3":
                self.view_balance()
            elif choice == "4":
                self.history()
            elif choice == "5":
                print("Exit")
                break
            else:
                print("Invalid aoption, try again")

call = Finance_tracker()
call.output()