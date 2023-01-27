
import calculation as calc
import exceptions as exc
from logg import logging


def main_menu():

    print('\n You are in CALCULATOR\n')
    while True:
        number_type = input('Choose the type of inputting numbers: \n'
                            'R - rational\n'
                            'C - complex\n'
                            'exit - for exit from CALCULATOR\n')
        match number_type:
            case 'R' | 'C':
                calculator_menu(number_type)
            case 'exit':
                logging.info("Program is stopped.")
                print("CALCULATOR is closed")
                break
            case _:
                logging.warning("Main menu: wrong number type selected.")
                print('Wrong number type. Please input again')


def calculator_menu(num_type):

    logging.info("Enter calculator menu")

    while True:
        operation = input('Choose operation: \n'
                            ' "+"  for summation\n'
                            ' "-" for subtraction\n'
                            ' "*"  for multiplication\n'
                            ' "/"  for division\n'
                            '"exit"  for exit to main menu\n')
        if not exc.input_sign_check(operation):
            break
        if operation == 'exit':
            logging.info('Exit to main menu\n')
            break

        if num_type == 'R':
            num_1, num_2 = input('Input first number: '), input('Input second number: ')
            if exc.input_num_check(num_1) and exc.input_num_check(num_2):
                num_1, num_2 = float(num_1), float(num_2)
            else:
                break
        elif num_type == 'C':

            print('Enter first complex number: \n')
            num_1_1, num_1_2 = input('Input part 1: '), input('Input part 2: ')
            if exc.input_num_check(num_1_1) and exc.input_num_check(num_1_2):
                num_1 = complex(float(num_1_1), float(num_1_2))
            else:
                break
            print('Enter second complex number: \n')
            num_2_1, num_2_2 = input('Input part 1: '), input('Input part 2: ')
            if exc.input_num_check(num_2_1) and exc.input_num_check(num_2_2):
                num_2 = complex(float(num_2_1), float(num_2_2))
            else:
                break

        match operation:
            case '+':
                result = calc.summation(num_1, num_2)
                logging.info(f"Summation: {num_1} + {num_2} = {result}")
            case '-':
                result = calc.subtraction(num_1, num_2)
                logging.info(f"Subtraction: {num_1} - {num_2} = {result}")
            case '*':
                result = calc.multiplication(num_1, num_2)
                logging.info(f"Multiplication: {num_1} * {num_2} = {result}")
            case '/':
                if not exc.division_0(num_2):
                    break
                result = calc.division(num_1, num_2)
                logging.info(f"Division: {num_1} / {num_2} = {result}")
            # case 'exit':
            #     logging.info('Exit to main menu\n')
            #     break
            case _:
                logging.warning("Calculator menu: wrong operation selected.")
                print('Wrong operation selected. Please input again')
                continue

        print(f'\n{num_1} {operation} {num_2} = {result}', end='\n\n')
