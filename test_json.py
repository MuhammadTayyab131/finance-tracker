class Finance_tracker:
    def __init__(self):
        self.transactions = []

    def get_amount(self):
        while True:
            amount = input("Enter amount: ")
            try:
                amount = float(amount)
                if amount <= 0:
                    print("Amount must be greater than zero!")
                else:
                    return amount
            except ValueError:
                print("Please enter a valid number.")

    # Get category from user
    def get_category(self):
        category = input("Enter category (e.g., food, transport, salary): ").strip()
        if category == "":
            category = "Other"
        return category

    # Add income
    def add_income(self):
        amount = self.get_amount()
        category = self.get_category()
        self.transactions.append({
            "type": "income",
            "amount": amount,
            "category": category
        })
        print("Income added successfully!")

    # Calculate balance
    def get_balance(self):
        balance = 0
        for t in self.transactions:
            if t["type"] == "income":
                balance += t["amount"]
            else:
                balance -= t["amount"]
        return balance

    # Add expense
    def add_expense(self):
        amount = self.get_amount()
        balance = self.get_balance()
        if amount > balance:
            print("Expense exceeding current balance!")
            return
        category = self.get_category()
        self.transactions.append({
            "type": "expense",
            "amount": amount,
            "category": category
        })
        print("Expense added successfully!")

    # View balance
    def view_balance(self):
        balance = self.get_balance()
        print(f"Current Balance: {balance}")

    # View transaction history
    def history(self):
        if not self.transactions:
            print("No transactions found yet.")
            return
        for j, t in enumerate(self.transactions, start=1):
            print(f"{j}. {t['type'].capitalize()} - {t['amount']} - Category: {t['category']}")

    # Show menu
    def show_menu(self):
        print("\nPersonal Finance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Transaction History")
        print("5. Exit")

    # Main loop
    def output(self):
        while True:
            self.show_menu()
            choice = input("Choose an option: ")
            if choice == "1":
                self.add_income()
            elif choice == "2":
                self.add_expense()
            elif choice == "3":
                self.view_balance()
            elif choice == "4":
                self.history()
            elif choice == "5":
                print("Exit")
                break
            else:
                print("Invalid option, try again.")

# Run the program
call = Finance_tracker()
call.output()
