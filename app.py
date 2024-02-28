from services.exchange_rate_service import ExchangeRateService
from utils.csv_parser import update_rates_from_csv

def main():
    # Initialize the exchange rate service
    exchange_rate_service = ExchangeRateService()

    # Update rates from the CSV file
    update_rates_from_csv(exchange_rate_service)

    # Continue with the rest of your application logic

if __name__ == "__main__":
    main()
