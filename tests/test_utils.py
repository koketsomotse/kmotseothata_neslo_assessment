#neobank_transfers/tests/test_utils.py
import unittest
from utils.csv_parser import load_exchange_rates

class TestCSVParser(unittest.TestCase):
    def test_load_exchange_rates(self):
        # This test would require a sample CSV file with known content
        # For simplicity, let's assume it's called "sample_rates.csv"
        # and contains USD,EUR,0.88 among its rates
        rates = load_exchange_rates("path/to/sample_rates.csv")
        self.assertIn(("USD", "EUR"), rates)
        self.assertEqual(rates[("USD", "EUR")], 0.88)

if __name__ == '__main__':
    unittest.main()
