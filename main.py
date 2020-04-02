from atm import DepositAccount, NormalSavingsAccount, ZeroMaintainingSavingsAccount, SuperSavingsAccount, AccountDatabase
import json

'''
Hard-coded object test cases to try

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
'''

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
        withdraw_from_account()

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

            try:
                deposit_amount = int(input('Amount to Deposit: '))
                account.deposit(deposit_amount)
            except ValueError:
                print('Invalid input')
            else:
                print(
                    f'Successfully deposited money, new balance is {account.readable_balance()}')

    input('Press ENTER to continue...')
    MainMenu()


def withdraw_from_account():
    pass


MainMenu()


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
