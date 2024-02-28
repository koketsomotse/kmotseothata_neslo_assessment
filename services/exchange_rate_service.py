#neobank_transfers/services/exchange_rate_service.py
# services/exchange_rate_service.py
# services/exchange_rate_service.py
class ExchangeRateService:
    def __init__(self):
        # Initialize with some default rates; you might replace these with actual API calls or CSV loading
        self.rates = {
            "USD": 1.0,  # Assuming USD is the base rate
            "EUR": 0.9,
            "GBP": 0.8,
        }

    def get_rate(self, currency):
        """
        Retrieves the exchange rate for a given currency.

        :param currency: The currency code as a string (e.g., 'USD', 'EUR').
        :return: The exchange rate as a float.
        """
        return self.rates.get(currency, None)

    def set_rate(self, currency, rate):
        """
        Updates or sets the exchange rate for a given currency.

        :param currency: The currency code as a string (e.g., 'USD', 'EUR').
        :param rate: The exchange rate as a float.
        """
        self.rates[currency] = rate
        print(f"Rate updated: {currency} = {rate}")

    def update_rates_from_api(self):
        """
        Placeholder method for updating rates from an external API.
        In a real scenario, you would implement the API call here.
        """
        # Mock update from API
        self.set_rate("USD", 1.0)
        self.set_rate("EUR", 0.85)
        self.set_rate("GBP", 0.75)
        print("Rates updated from API.")

# Example usage
if __name__ == "__main__":
    exchange_rate_service = ExchangeRateService()
    print(exchange_rate_service.get_rate("EUR"))  # Example of getting a rate

    # Update a rate manually
    exchange_rate_service.set_rate("CAD", 1.25)
    print(exchange_rate_service.get_rate("CAD"))

    # Mock updating rates from an API
    exchange_rate_service.update_rates_from_api()
