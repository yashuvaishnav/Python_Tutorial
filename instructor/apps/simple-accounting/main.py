import datetime
import json

class Account:
    def __init__(self, name, account_type):
        self.name = name
        self.account_type = account_type  # Asset, Liability, Equity, Revenue, Expense
        self.balance = 0.0
        self.ledger = []

    def debit(self, amount, description):
        self.balance += amount
        self.ledger.append((datetime.datetime.now(), "Debit", amount, description))

    def credit(self, amount, description):
        self.balance -= amount
        self.ledger.append((datetime.datetime.now(), "Credit", amount, description))

    def __str__(self):
        return f"{self.name} ({self.account_type}): ${self.balance:.2f}"

class JournalEntry:
    def __init__(self, date, description):
        self.date = date
        self.description = description
        self.entries = []  # List of tuples (Account, amount, type)

    def add_entry(self, account, amount, entry_type):
        self.entries.append((account, amount, entry_type))
        if entry_type == 'debit':
            account.debit(amount, self.description)
        elif entry_type == 'credit':
            account.credit(amount, self.description)

    def __str__(self):
        return f"{self.date} - {self.description}\n" + "\n".join([f"  {acc.name}: {amt} ({typ})" for acc, amt, typ in self.entries])

class AccountingSystem:
    def __init__(self):
        self.accounts = {}
        self.journal_entries = []

    def create_account(self, name, account_type):
        if name in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[name] = Account(name, account_type)
            print(f"Account '{name}' created.")

    def record_transaction(self, date, description, transactions):
        journal_entry = JournalEntry(date, description)
        debit_total = 0
        credit_total = 0

        for acc_name, amount, entry_type in transactions:
            if acc_name in self.accounts:
                account = self.accounts[acc_name]
                journal_entry.add_entry(account, amount, entry_type)
                if entry_type == 'debit':
                    debit_total += amount
                elif entry_type == 'credit':
                    credit_total += amount
            else:
                print(f"Account '{acc_name}' not found.")
                return

        if debit_total != credit_total:
            print("Error: Debit and Credit amounts do not match. Transaction aborted.")
            return

        self.journal_entries.append(journal_entry)
        print("Transaction recorded successfully.")

    def generate_balance_sheet(self):
        print("\nBalance Sheet")
        print("----------------------")
        for acc in self.accounts.values():
            if acc.account_type in ['Asset', 'Liability', 'Equity']:
                print(acc)

    def generate_income_statement(self):
        print("\nIncome Statement")
        print("----------------------")
        for acc in self.accounts.values():
            if acc.account_type in ['Revenue', 'Expense']:
                print(acc)

    def list_accounts(self):
        print("\nAccounts")
        print("----------------------")
        for acc in self.accounts.values():
            print(acc)

    def list_journal_entries(self):
        print("\nJournal Entries")
        print("----------------------")
        for je in self.journal_entries:
            print(je)

    def view_ledger(self, account_name):
        if account_name in self.accounts:
            acc = self.accounts[account_name]
            print(f"\nLedger for {acc.name}")
            print("----------------------")
            for entry in acc.ledger:
                print(f"{entry[0]} - {entry[1]}: ${entry[2]:.2f} ({entry[3]})")
        else:
            print("Account not found.")

if __name__ == "__main__":
    system = AccountingSystem()

    while True:
        print("\nAccounting System Menu")
        print("1. Create Account")
        print("2. Record Transaction")
        print("3. Generate Balance Sheet")
        print("4. Generate Income Statement")
        print("5. List Accounts")
        print("6. List Journal Entries")
        print("7. View Ledger")
        print("8. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            name = input("Enter account name: ")
            account_type = input("Enter account type (Asset, Liability, Equity, Revenue, Expense): ")
            system.create_account(name, account_type)
        
        elif choice == "2":
            date = input("Enter transaction date (YYYY-MM-DD): ")
            description = input("Enter transaction description: ")
            transactions = []
            while True:
                acc_name = input("Enter account name: ")
                amount = float(input("Enter amount: "))
                entry_type = input("Enter type (debit/credit): ")
                transactions.append((acc_name, amount, entry_type))
                more = input("Add more entries? (y/n): ")
                if more.lower() != 'y':
                    break
            system.record_transaction(date, description, transactions)
        
        elif choice == "3":
            system.generate_balance_sheet()
        
        elif choice == "4":
            system.generate_income_statement()
        
        elif choice == "5":
            system.list_accounts()
        
        elif choice == "6":
            system.list_journal_entries()
        
        elif choice == "7":
            acc_name = input("Enter account name: ")
            system.view_ledger(acc_name)
        
        elif choice == "8":
            print("Exiting system.")
            break
        
        else:
            print("Invalid choice. Please try again.")
