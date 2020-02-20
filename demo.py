# Обмен валют
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


def currency_exchange_2(money_2, currency_2):
    for key, value in currencies_2.items():
        if currency_2 in key:
            return value * money_2
        else:
            return f"Sorry! Not available currency for {currency_2}"


print(currency_exchange_2(100, 'usa'))
print('')
input('Press any key to exit')
