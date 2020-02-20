
def currency_exchange_2(money_2, currency_2):
    currencies_2 = {
        'USD': 0.041,
        'EUR': 0.038,
        'RUB': 2.6,
        'JPY': 4.57,
        'GBP': 0.032,
        'CHF': 0.04,
        'CAD': 0.054,
        'AUD': 0.062
    }
    for key, value in currencies_2.items():
        if currency_2 in key:
            return f"{money_2} UAH = {round(value * money_2, 2)} {currency_2}"
        else:
            return f"Sorry! Not available for currency {currency_2}! "


# Enter money

while True:
    try:
        amount_2 = int(input('Enter the amount in UAH  '))
        break
    except ValueError:
        print("Not an integer! Please enter an integer")

# Now let user choose an available currency
my_currency_2 = input('Enter one of the available currencies (USD, EUR, RUB, JPY, GBP, CHF, CAD, AUD ) -  ')

print(currency_exchange_2(amount_2, my_currency_2))
print('')
input('Press any key to exit')
