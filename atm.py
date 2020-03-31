# ATM classes
# by Ron Divina

# SECTION I - Class Definitions

# 1. This is "atm.py", and put all succeeding class definitions in this file.

# 2. Create a base class, DepositAccount, containing attributes: account_id, account_type, full_name, birthday, balance, and maintaining_balance


class DepositAccount:
    def __init__(self, account_id, account_type, full_name, birthday, balance, maintaining_balance):
        self.account_id = account_id
        self.account_type = account_type
        self.full_name = full_name
        self.birthday = birthday
        self.balance = balance
        self.maintaining_balance = maintaining_balance


# The base class should have the following function "display_info" which prints the account information in the following format:

# Account ID: [account id]
# Full Name: [full name]
# Account Type: [account type in readable format, * see details below]
# Age: [computed age based on birthday]
# Balance: [balance in readable format, ** see details below]


# * - Deposit Account Types:
# NSA = Normal Savings Account
# ZMSA = Zero Maintaining Savings Account
# SSA = Super Savings Account

# ** - Balance in readable format should be in P#,###.## e.g. P5,423,523.80

# E.g.

# Account ID: ph-342851
# Full Name: Juan Dela Cruz
# Account Type: Zero Maintaining Savings Account
# Age: 29
# Balance: P65,536.00


# The base class should also have the following functions, "withdraw" and "deposit" which accepts the parameter "amount"

# For the withdraw function, you should subtract the amount from the current balance.

# For the deposit function, you should add the amount to the current balance.


# 3. For each deposit account, create a child class which inherits from DepositAccount class:
# - NormalSavingsAccount for Normal Savings Account
# - ZeroMaintainingSavingsAccount for Zero Maintaining Savings Account
# - SuperSavingsAccount for Super Savings Account

# NormalSavingsAccount class should set the attribute maintaining_balance to 3000 and should override the "withdraw" function. Apply the withdraw logic from the description:
# - If the user withdraws money and if the balance is below P3,000, the system will deduct P100 on top of the withdrawn amount, and will display a warning, "Warning: Account is below maintaining balance.").

# ZeroMaintainingSavingsAccount class should set the attribute maintaining_balance to 0 and should override the "withdraw" function. Apply the logic from the description:
# - Withdrawal fee is P12 i.e. the system will deduct P12 on top of the withdrawn amount each time the user withdraws money.

# SuperSavingsAccount class should set the attribute maintaining_balance to 100000 and should override the "withdraw" function. Apply the logic from the description:
# - If the user withdraws money and if the balance is below P100,000, the system will deduct P100 on top of the withdrawn amount, and will display a warning that it's below maintaining.

# SuperSavingsAccount class should also override the "deposit" function and apply the logic from the description:
# - Every time the user deposits money, there's a bonus of 2% on top of the deposited amount. E.g. if the user deposits P10,000 the system will add a bonus of P200.

# 4. Create a class "AccountDatabase" which has an attribute "accounts" which is an list / array that will contain DepositAccount objects. You may add more attributes and functions as you see fit to complete the rest of the requirements.
