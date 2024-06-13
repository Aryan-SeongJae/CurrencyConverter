import requests

def get_exchange_rates(api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        raise Exception("Error fetching exchange rates: " + data.get("error-type", "Unknown error"))
    return data['conversion_rates']

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency != 'USD':
        amount = amount / rates[from_currency]
    converted_amount = amount * rates[to_currency]
    return converted_amount

def main():
    api_key = 'be88d21f7262098aa66b3be2'  # Replace with your actual API key from exchangerate-api.com
    rates = get_exchange_rates(api_key)

    from_currency = input("Enter the currency you want to convert from (e.g., EUR, GBP, INR): ").upper()
    to_currency = input("Enter the currency you want to convert to (e.g., EUR, GBP, INR): ").upper()
    amount = float(input("Enter the amount you want to convert: "))

    if from_currency not in rates or to_currency not in rates:
        print("Invalid currency code.")
        return

    converted_amount = convert_currency(amount, from_currency, to_currency, rates)
    amount_in_usd = convert_currency(amount, from_currency, 'USD', rates)

    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    print(f"{amount} {from_currency} is equal to {amount_in_usd:.2f} USD")


    x = input("Do you want to convert another currency? (yes/no): ")
    if x == "yes":
        main()
    else:
        print("Thank you for using the currency converter!")

if __name__ == "__main__":
    main()
