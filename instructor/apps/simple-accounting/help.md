Here’s a dry run of the updated accounting system to maintain and track expenses over time.

# Step 1: Create Accounts
We need to create the following accounts:

- Cash (Asset)
- Bank (Asset)
- Expenses (Expense)
- Revenue (Revenue)

## Commands & Output

1. Create Account
Enter account name: Cash
Enter account type (Asset, Liability, Equity, Revenue, Expense): Asset
Account 'Cash' created.

1. Create Account
Enter account name: Bank
Enter account type (Asset, Liability, Equity, Revenue, Expense): Asset
Account 'Bank' created.

1. Create Account
Enter account name: Expenses
Enter account type (Asset, Liability, Equity, Revenue, Expense): Expense
Account 'Expenses' created.

1. Create Account
Enter account name: Revenue
Enter account type (Asset, Liability, Equity, Revenue, Expense): Revenue
Account 'Revenue' created.

# Step 2: Record Transactions
Let's simulate some real-world transactions.

1️⃣ Received Salary - ₹10,000 credited to Bank
This means:

Debit (Increase) Bank ₹10,000
Credit (Increase) Revenue ₹10,000

2. Record Transaction
Enter transaction date (YYYY-MM-DD): 2025-02-01
Enter transaction description: Salary received
Enter account name: Bank
Enter amount: 10000
Enter type (debit/credit): debit
Enter account name: Revenue
Enter amount: 10000
Enter type (debit/credit): credit
Transaction recorded successfully.

2️⃣ Paid Rent - ₹5,000 deducted from Bank
This means:

Debit (Increase) Expenses ₹5,000
Credit (Decrease) Bank ₹5,000

2. Record Transaction
Enter transaction date (YYYY-MM-DD): 2025-02-05
Enter transaction description: Paid Rent
Enter account name: Expenses
Enter amount: 5000
Enter type (debit/credit): debit
Enter account name: Bank
Enter amount: 5000
Enter type (debit/credit): credit
Transaction recorded successfully.

3️⃣ Withdraw Cash from Bank - ₹2,000
This means:

Debit (Increase) Cash ₹2,000
Credit (Decrease) Bank ₹2,000

2. Record Transaction
Enter transaction date (YYYY-MM-DD): 2025-02-10
Enter transaction description: Cash withdrawn from Bank
Enter account name: Cash
Enter amount: 2000
Enter type (debit/credit): debit
Enter account name: Bank
Enter amount: 2000
Enter type (debit/credit): credit

Transaction recorded successfully.

# Step 3: View Accounts & Balances
Now, let's list all account balances.

5. List Accounts
----------------------
Cash (Asset): ₹2,000
Bank (Asset): ₹3,000
Expenses (Expense): ₹5,000
Revenue (Revenue): ₹10,000

# Step 4: View Ledger for 'Bank'

7. View Ledger
Enter account name: Bank
----------------------
2025-02-01 - Debit: ₹10,000 (Salary received)
2025-02-05 - Credit: ₹5,000 (Paid Rent)
2025-02-10 - Credit: ₹2,000 (Cash withdrawn from Bank)

# Step 5: Generate Balance Sheet

3. Generate Balance Sheet
----------------------
Cash (Asset): ₹2,000
Bank (Asset): ₹3,000

# Step 6: Generate Income Statement
4. Generate Income Statement
----------------------
Expenses (Expense): ₹5,000
Revenue (Revenue): ₹10,000
Final Status
- ✅ Total Assets = ₹5,000 (₹2,000 in Cash + ₹3,000 in Bank)
- ✅ Total Income = ₹10,000
- ✅ Total Expenses = ₹5,000
- ✅ Net Profit = ₹5,000 (Revenue - Expenses)

Summary
- Tracked salary income and credited it to Bank.
- Paid rent, reducing Bank balance and increasing Expenses.
- Withdrawn cash, shifting funds from Bank to Cash.
- Viewed ledgers, account balances, and financial reports.

This system now fully supports expense tracking, financial reports, and cash flow management over time! 🚀