# utils/csv_parser.py

import csv

def update_rates_from_csv(exchange_rate_service, filepath='exchange_rates.csv'):
    """
    Updates the exchange rates in the exchange_rate_service using data from a CSV file.

    :param exchange_rate_service: The exchange rate service instance to update.
    :param filepath: The path to the CSV file containing exchange rates.
    """
    with open(filepath, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            currency = row['currency']
            rate = float(row['rate'])
            exchange_rate_service.set_rate(currency, rate)
    print(f"Updated rates from CSV: {exchange_rate_service.rates}")
