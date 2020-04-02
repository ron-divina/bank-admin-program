from atm import DepositAccount, NormalSavingsAccount, ZeroMaintainingSavingsAccount, SuperSavingsAccount, AccountDatabase
import json

d = DepositAccount('0', None, 'Kana Yoshida', 'September 18, 2002', 3000)
d1 = NormalSavingsAccount('1', 'NSA', 'Ron Divina', 'August 10, 1999', 5000)
d2 = ZeroMaintainingSavingsAccount(
    '2', 'ZMSA', 'Geo Hotz', 'July 5, 1993', 4000)
d3 = SuperSavingsAccount('3', 'SSA', 'Elon Musk', 'June 28, 1971', 69420)

account_db = AccountDatabase()

account_db.add_account(d)
account_db.add_account(d1)
account_db.add_account(d2)
account_db.add_account(d3)


account_db_json = AccountDatabase()

with open('accounts.json', 'r') as myfile:
    data = myfile.read()

json = json.loads(data)

for account in json['accounts']:
    if account['account_type'] == 'NSA':
        new_account = NormalSavingsAccount(
            account['account_id'], account['account_type'], account['full_name'], account['birthday'], account['balance'])
    if account['account_type'] == 'ZMSA':
        new_account = ZeroMaintainingSavingsAccount(
            account['account_id'], account['account_type'], account['full_name'], account['birthday'], account['balance'])
    if account['account_type'] == 'SSA':
        new_account = SuperSavingsAccount(
            account['account_id'], account['account_type'], account['full_name'], account['birthday'], account['balance'])

    account_db_json.add_account(new_account)

# print(account_db.show_accounts_dict())
# print(account_db.show_accounts_list())

# print(account_db_json.show_accounts_dict())
# print(account_db_json.show_accounts_list())


def MainMenu():

    print('''
 ============================================================
 ==============================
 Welcome to Pai Bank ATM Admin
 ==============================

 ( 1 ) List All Accounts
 ( 2 ) Deposit Money to an Account
 ( 3 ) Withdraw Money from an Account
 ( 4 ) Exit
 ''')

    user_input = int(input("Input choice: "))
    print('============================================================')

    if user_input == 1:
        list_all_accounts()

    if user_input == 2:
        deposit_to_account()

    if user_input == 3:
        pass

    if user_input == 4:
        exit()


def list_all_accounts():
    for account in account_db_json.accounts:
        print(account.display_info())

    input('Press ENTER to continue...')
    MainMenu()


def deposit_to_account():
    account_id_input = input('Enter Account ID: ')

    for account in account_db_json.accounts:
        if account_id_input == account.account_id:
            print(account.display_info())

            deposit_amount = int(input('Amount to Deposit: '))
            account.deposit(deposit_amount)
            print(
                f'Successfully deposited money, new balance is {account.balance}')


MainMenu()

# SECTION III - Main Menu

# (You have the option to make the Main Menu a separate class but it's not required)

# 1. After reading the data, display the Main Menu to the user:

# Main Menu:

# ============================================================
# ==============================
# Welcome to Pai Bank ATM Admin
# ==============================

# ( 1 ) List All Accounts
# ( 2 ) Deposit Money to an Account
# ( 3 ) Withdraw Money from an Account
# ( 4 ) Exit

# Input choice:
# ============================================================

# Note that "============================================================" is not required to be displayed, it's just a way to indicate that it's a program display. This is true for all program examples. Displaying or not displaying it will not affect your grade.


# 2. When user inputs "1" and presses enter, enumerate all accounts using the format:

# [count starting 1].
# Account ID: [account id]
# Full Name: [full name]
# Account Type: [account type in readable format]
# Age: [computed age based on birthday]
# Balance: [balance in readable format

# E.g.

# ============================================================
# 1.
# Account ID: ph-342851
# Full Name: Juan Dela Cruz
# Account Type: Zero Maintaining Savings Account
# Age: 29
# Balance: P65,536.00

# 2.
# Account ID: ph-552322
# Full Name: Angelo Martin
# Account Type: Normal Savings Account
# Age: 20
# Balance: P32,768.38

# 3.
# Account ID: ph-252124
# Full Name: Christine Santos
# Account Type: Super Savings Account
# Age: 36
# Balance: P2,147,483.50

# Press enter key to return to main menu..
# ============================================================


# When system has finished displaying all the accounts, user needs to press enter and the program will display the main menu.

# Note that at this point, if you've done your classes correctly, you just need to call each object's display_info function after display the correct count.


# 3. When user inputs "2" and presses enter, the program will ask the user to input the Account ID.

# User will need to enter a specific account ID e.g. "ph-342851"

# The program will look for the deposit account object in the AccountDatabase with the account ID and display the information of the account (i.e. call the object's display_info function).

# The program will then ask for the amount of money to deposit and when the user inputs the amount and presses enter, the system will deduct the amount to the account's balance following the logic of each deposit account, and display the new balance information. At this point, if you've done your classes correctly, you just need to call the withdraw function of the object passing the amount.

# E.g.

# ============================================================
# Input Account ID: ph-342851

# Account ID: ph-342851
# Full Name: Juan Dela Cruz
# Account Type: Zero Maintaining Savings Account
# Age: 29
# Balance: P65,536.00

# Amount to Deposit: 1000

# Successfully deposited money, new balance is P66,536.00

# Press enter key to return to main menu..
# ============================================================


# Pressing enter will go back to the main menu screen.

# For simplicity, it is not required to handle invalid account ID's (but you may do so if you feel like it).


# 4. When user inputs "3" and presses enter, the program will ask the user to input the Account ID.

# User will need to enter a specific account ID e.g. "ph-342851"

# The program will look for the deposit account object in the AccountDatabase with the account ID and display the information of the account (i.e. call the object's display_info function).

# The program will then ask for the amount of money to withdraw and when the user inputs the amount and presses enter, the system will deduct the amount to the account's balance, following the logic of each deposit account, and display the new balance information. At this point, if you've done your classes correctly, you just need to call the withdraw function of the object passing the amount.

# E.g.

# ============================================================
# Input Account ID: ph-342851

# Account ID: ph-342851
# Full Name: Juan Dela Cruz
# Account Type: Zero Maintaining Savings Account
# Age: 29
# Balance: P65,536.00

# Amount to Withdraw: 1000

# Successfully withdrawn money, new balance is P64,524.00

# Press enter key to return to main menu..
# ============================================================


# Pressing enter will go back to the main menu screen.

# For simplicity, it is not required to handle invalid account ID's (but you may do so if you feel like it).


# 5. When user inputs "4" and presses enter, the program will exit.
