from helpers import get_currencies, print_currencies, validate_currencies, \
    validate_amount, get_exchange_rate_or_convert
from constants import Colors


def main():
    """
    Initialise program
    """
    print(f'\n{Colors.label}Welcome to Currency Converter!{Colors.reset}')
    print()
    print(f'{Colors.text_bold}Commands:{Colors.reset}')
    print(f'{Colors.text_bold} * List{Colors.reset}{Colors.text} - print all available currencies.')
    print(f'{Colors.text_bold} * Rate{Colors.reset}{Colors.text} - get exchange rate of two currencies.')
    print(f'{Colors.text_bold} * Convert{Colors.reset}{Colors.text} - convert one currency to another.')
    print(f'{Colors.text_bold} * Q{Colors.reset}{Colors.text} - to quit.')
    print(f" * Enter currency {Colors.text_bold}code{Colors.reset}{Colors.text} to get it's name{Colors.reset}")
    currencies = get_currencies()

    # running loop while command entered is not 'q'
    while True:
        command = input(f'\n{Colors.bold}Enter a command: {Colors.reset}').lower()

        # check if command id currency code to get it's name
        if command.upper() in currencies:
            print(Colors.label + currencies[command.upper()]['description'] + Colors.reset)

        # command to print all currencies and names
        elif command == 'list':
            print()
            print_currencies(currencies)

        # command to convert or get rate
        elif command == 'rate' or command == 'convert':
            base = validate_currencies(currencies)
            if base:
                currency = validate_currencies(currencies, currency_type='currency to convert to')
                if currency:

                    # if command is 'rate' just print rate
                    if command == 'rate':
                        get_exchange_rate_or_convert(base, currency)
                    
                    # if command is 'convert' - get amount and convert
                    else:
                        amount = validate_amount(base)
                        if amount:
                            get_exchange_rate_or_convert(base, currency, amount)
        
        # terminate loop
        elif command == 'q':
            break
        
        # if command is none of the above print error message
        else:
            print(f'{Colors.errors}Invalid command. Please try again.{Colors.reset}')


if __name__ == '__main__':
    import os
    os.system('color')
    main()
