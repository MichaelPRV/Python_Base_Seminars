
from logg import logging


def input_sign_check(sign):
    sign.replace(' ', '')
    if sign in ['+', '-', '*', '/', 'exit']:
        return True
    else:
        logging.warning("Incorrect sign input")
        print(f'\nIncorrect sign input: "{sign}". Try again\n')
        return False


def input_num_check(number):
    if number.replace(' ', '').replace('.', '', 1).isdigit():
        return True
    else:
        logging.warning("Incorrect number input")
        print(f'\nIncorrect number input: "{number}". Try again\n')
        return False


def division_0(divider):
    if not divider:
        print("\nError: division by 0. Input another divider\n")
        return False
