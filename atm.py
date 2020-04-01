class DepositAccount:
    def __init__(self, account_id, account_type, full_name, birthday, balance):
        self.account_id = account_id
        self.account_type = account_type
        self.full_name = full_name
        self.birthday = birthday
        self.balance = balance
        self.maintaining_balance = 0

    def display_info(self):
        from datetime import datetime, date

        if self.account_type == 'NSA':
            self.account_type = 'Normal Savings Account'
        elif self.account_type == 'ZMSA':
            self.account_type = 'Zero Maintaining Savings Account'
        elif self.account_type == 'SSA':
            self.account_type = 'Super Savings Account'

        birth_date = datetime.strptime(self.birthday, "%B %d, %Y")
        today = date.today()
        age = today.year - birth_date.year - \
            ((today.month, today.day) < (birth_date.month, birth_date.day))

        balance_readable_format = "₱{:,.2f}".format(self.balance)

        return f"""
        Account ID: {self.account_id}
        Full Name: {self.full_name}
        Account Type: {self.account_type}
        Age: {age}
        Balance: {balance_readable_format}
        """

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


class NormalSavingsAccount(DepositAccount):
    def __init__(self, account_id, account_type, full_name, birthday, balance):
        super().__init__(account_id, account_type, full_name, birthday, balance)
        self.maintaining_balance = 3000

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 3000:
            print('Warning: Account is below maintaining balance.')
            self.balance -= 100


class ZeroMaintainingSavingsAccount(DepositAccount):
    def __init__(self, account_id, account_type, full_name, birthday, balance):
        super().__init__(account_id, account_type, full_name,
                         birthday, balance)

    def withdraw(self, amount):
        self.balance -= amount
        self.balance -= 12


class SuperSavingsAccount(DepositAccount):
    def __init__(self, account_id, account_type, full_name, birthday, balance):
        super().__init__(account_id, account_type, full_name,
                         birthday, balance)
        self.maintaining_balance = 100000

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 100000:
            print('Warning: Account is below maintaining balance.')
            self.balance -= 100

    def deposit(self, amount):
        bonus = amount * (2 / 100)
        self.balance += amount
        self.balance += bonus


class AccountDatabase:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def show_accounts_list(self):
        accounts = []
        for account in self.accounts:
            accounts.append(account.full_name + ':' +
                            str(account.account_type))

        return accounts

    def show_accounts_dict(self):
        accounts = dict()
        for account in self.accounts:
            accounts[account.full_name] = str(account.account_type)

        return accounts


d = DepositAccount(0, None, 'Kana Yoshida', 'September 18, 2002', 3000)
d1 = NormalSavingsAccount(1, 'NSA', 'Ron Divina', 'August 10, 1999', 5000)
d2 = ZeroMaintainingSavingsAccount(2, 'ZMSA', 'Geo Hotz', 'July 5, 1993', 4000)
d3 = SuperSavingsAccount(3, 'SSA', 'Elon Musk', 'June 28, 1971', 69420)

account_db = AccountDatabase()

account_db.add_account(d)
account_db.add_account(d1)
account_db.add_account(d2)
account_db.add_account(d3)

print(account_db.show_accounts_list())
print(account_db.show_accounts_dict())
