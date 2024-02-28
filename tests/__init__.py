import pytest
from models.account import Account
from models.transaction import Transaction

def test_transaction_negative_amount():
    account_a = Account("User A", "123", 1000, "USD")
    account_b = Account("User B", "456", 800, "EUR")
    with pytest.raises(ValueError):
        Transaction(account_a, account_b, -100, "USD")
