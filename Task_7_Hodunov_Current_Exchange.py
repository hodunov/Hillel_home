# Обмен валют


def currency_exchange(money, currency):
    currencies = {
        'USD': 0.041,
        'EUR': 0.038,
        'RUB': 2.6,
        'JPY': 4.57,
        'GBP': 0.032,
        'CHF': 0.04,
        'CAD': 0.054,
        'AUD': 0.062
    }
    for key, value in currencies.items():
        if currency in key:
            return f"{money} UAH = {round(value * money,2)} {currency}"


# Enter money

while True:
    try:
        amount = int(input('Enter the amount in UAH  '))
        break
    except ValueError:
        print("Not an integer! Please enter an integer")

# Now let user choose an available currency

currency_list = ('USD', 'EUR', 'RUB', 'JPY', 'GBP', 'CHF', 'CAD', 'AUD')
while True:
    print('Chose one of the available currencies: USD, EUR, RUB, JPY, GBP, CHF, CAD, AUD')
    my_currency = input('Enter currency type   ')
    if my_currency in currency_list:
        break
    else:
        print("Sorry! Not available currency!")

print(currency_exchange(amount, my_currency))
print('')
input('Press any key to exit')
