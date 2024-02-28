#neobank_transfers/models/transaction.py
class Transaction:
    def __init__(self, source_account, dest_account, amount, currency):
        self.source_account = source_account
        self.dest_account = dest_account
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"Transaction(source_account={self.source_account}, dest_account={self.dest_account}, amount={self.amount}, currency={self.currency})"
