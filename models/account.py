#neobank_transfers/models/account.py
class Account:
    def __init__(self, owner, account_number, balance, currency):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
        self.currency = currency

    def __str__(self):
        return f"Account(owner={self.owner}, account_number={self.account_number}, balance={self.balance}, currency={self.currency})"
