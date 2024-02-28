#neobank_transfers/tests/test_models.py
import unittest
from models.account import Account
from models.transaction import Transaction

class TestAccountModel(unittest.TestCase):
    def test_account_creation(self):
        account = Account(owner="John Doe", account_number="12345678", balance=1000, currency="USD")
        self.assertEqual(account.owner, "John Doe")
        self.assertEqual(account.account_number, "12345678")
        self.assertEqual(account.balance, 1000)
        self.assertEqual(account.currency, "USD")

class TestTransactionModel(unittest.TestCase):
    def test_transaction_creation(self):
        transaction = Transaction(source_account="12345678", dest_account="87654321", amount=100, currency="USD")
        self.assertEqual(transaction.source_account, "12345678")
        self.assertEqual(transaction.dest_account, "87654321")
        self.assertEqual(transaction.amount, 100)
        self.assertEqual(transaction.currency, "USD")

if __name__ == '__main__':
    unittest.main()
