from os import path
import csv
from data_check import *
from logg import logging


phone_num_base = {}
last_id = 0
data_base_file = 'phonebook.csv'


def read_phonebook():
    global phone_num_base, last_id
    logging.info(f'Display phonebook from {data_base_file}')
    print(data_base_file)
    if path.exists(data_base_file):
        with open(data_base_file, 'r', encoding='utf-8') as book:
            csv_reader = csv.DictReader(book)
            phone_num_base = [num for num in csv_reader]
            last_id = phone_num_base[-1]['ID']
            return phone_num_base
    else:
        logging.warning('Phonebook file is not found')
        print('Phonebook file is not found')


def display_phonebook():
    display = ['  '.join(k.values()) for k in phone_num_base]
    print(*display, sep='\n', end='\n\n')


def edit_phone_number(edit_data, edit_id):
    global phone_num_base
    key, value = edit_data
    logging.info(f"Data changes: {edit_data}")
    if find_existing_contact(edit_id, phone_num_base):
        for i, v in enumerate(phone_num_base):
            if v["ID"] == edit_id:
                logging.info(f"Current value: {v[key]}")
                v[key] = value
                logging.info(f"New value: {v[key]}")
                phone_num_base[i] = v
        with open(data_base_file, "w", encoding="utf-8", newline="") as file:
            fields = ["ID", "name", "surname", "phonenumber", "info"]
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(phone_num_base)
            logging.info('Information is edited')
            print('Information is edited', end='\n')
    else:
        logging.warning(f"Inputted ID not exist: {edit_data}")
        print('Inputted ID not exist', end='\n')


def add_new_phone_number(data):
    global last_id
    logging.info(f'New phone number added: {data}')
    if all(data.values()) and duplication_check(data, phone_num_base):
        last_id = int(last_id) + 1
        data['ID'] = last_id
        with open(data_base_file, 'a', encoding='utf-8', newline='') as book:
            fields = ["ID", "name", "surname", "phonenumber", "info"]
            writer = csv.DictWriter(book, fieldnames=fields)
            writer.writerow(data)
            logging.warning(f'New phone number added: {data.values()}')
            print('New phone number added')
    else:
        logging.warning('Inputted data is duplicated')
        print('Inputted data is duplicated')


def delete_phone_number(for_deletion):
    global phone_num_base
    logging.info(f"Phone number deletion: {for_deletion}")
    num_id = find_existing_contact(for_deletion, phone_num_base)
    if num_id:
        id_for_del = input('Input ID: ')
        logging.info(f"ID selected: {id_for_del}")
        if id_for_del in num_id:
            phone_num_base = [k for k in phone_num_base if k["ID"] != id_for_del]
            with open(data_base_file, "w", encoding="utf-8", newline="") as file:
                fields = ["ID", "name", "surname", "phonenumber", "info"]
                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader()
                writer.writerows(phone_num_base)
                logging.info('Phone number is deleted')
                print('Phone number is deleted', end='\n')
        else:
            logging.warning(f"Inputted ID not exist: {for_deletion}")
            print('Inputted ID not exist', end='\n')
    else:
        logging.warning(f"Inputted ID not exist: {for_deletion}")


def import_file(name):
    global data_base_file
    logging.info(f"Import data base file: {name}")
    if path.exists(name):
        data_base_file = name
        print(data_base_file)
    else:
        logging.warning(f"File not found: {name}")
        print("File not found", end='\n')


def export_file(name):
    logging.info(f"Export {name}.csv")
    with open(f'{name}.csv', 'w', encoding="utf-8", newline="") as file_w, \
            open('phonebook.csv', encoding="utf-8") as file_r:
        all_data = csv.DictReader(file_r)
        fields = ["ID", "name", "surname", "phonenumber", "info"]
        writer = csv.DictWriter(file_w, fieldnames=fields)
        writer.writeheader()
        writer.writerows(phone_num_base)
        print(f"{name}.csv file saved\n")
