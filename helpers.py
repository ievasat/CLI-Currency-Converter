import requests
from constants import base_url, Colors


def get_currencies():
    endpoint = 'symbols'
    url = base_url + endpoint
    data = requests.get(url).json()
    return data['symbols']


def print_currencies(currencies):
    for key, value in currencies.items():
        name = value['description']
        print(f'{Colors.bold}{key}{Colors.reset} - {name}')
    return


def get_exchange_rate_or_convert(base, currency, amount=1.00):
    endpoint = f'convert?from={base}&to={currency}'
    url = base_url + endpoint
    data = requests.get(url).json()
    rate = data['info']['rate']
    if amount != 1:
        result = rate * amount
        print(f'{Colors.label}{amount:.2f} {base} --> {result:.2f} {currency}{Colors.reset}')
        return result
    else:
        print(f"{Colors.label}{base} --> {currency} = {rate}{Colors.reset}")
        return rate


def check_code(code, currencies):
    if code in currencies:
        return code
    print(f'{Colors.errors}Invalid currency code. Please try again.{Colors.reset}')
    return


def check_amount(amount):
    try:
        amount = float(amount)
        return amount
    except ValueError:
        print(f'{Colors.errors}Invalid amount. Please try again.{Colors.reset}')
        return


def validate_currencies(currencies, currency_type='base currency'):
    msg = f"Enter {currency_type} ('c' to cancel): "
    currency = None
    while currency is None:
        currency = input(msg).upper()
        if currency == 'C':
            return
        currency = check_code(currency, currencies)
    return currency


def validate_amount(base):
    amount = None
    while amount is None:
        amount = input(f"Enter amount in {Colors.bold}{base}{Colors.reset} ('c' to cancel): ")
        if amount.casefold() == 'c':
            return
        amount = check_amount(amount)
    return amount
