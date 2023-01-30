from processing import *
from data_check import new_contact_check


def user_menu():
    while True:
        read_phonebook()
        print(f"\n==========PHONEBOOK==========", end='\n\n')
        options = input("Choose option: \n"
                        "'1'  - display all contacts\n"
                        "'2'  - find contact\n"
                        "'3'  - edit contact\n"
                        "'4'  - add new contact\n"
                        "'5'  - delete contact\n"
                        "'6'  - import/export contacts\n"
                        "'7'  - exit the PHONEBOOK\n")
        match options:
            case "1":
                display_phonebook()
            case "2":
                find_existing_contact(input("Input surname or phone number: "), read_phonebook())
            case "3":
                display_phonebook()
                change_id = input("Input ID: ")
                if find_existing_contact(change_id, read_phonebook()) and (answer := contact_edit_menu()):
                    edit_phone_number(answer, change_id)
            case "4":
                add_new_phone_number(create_new_contact_menu())
            case "5":
                delete_phone_number(input("Input surname or phone number: "))
            case "6":
                import_export_menu()
            case "7":
                logging.info("Stop program.\n")
                print("PHONEBOOK is closed")
                break
            case _:
                logging.warning("Main menu, wrong option selected.")
                print("Incorrect input. Please try again ")


def contact_edit_menu():
    contacts_dict = {"1": "name", "2": "surname", "3": "phonenumber", "4": "info"}
    logging.info('Start contact edit menu')
    while True:
        print("\nChoose option: ")
        editing = input("'1'  - edit name\n"
                        "'2'  - edit surname\n"
                        "'3'  - edit phone\n"
                        "'4'  - edit info\n"
                        "'5'  - back to main menu\n")

        match editing:
            case "1" | "2" | "3" | "4":
                field = contacts_dict[editing]
                return field, new_contact_check(field)
            case "5":
                logging.info('Exit from edit contact edit menu')
                return 0
            case _:
                logging.warning("Contact edit menu: wrong option selected.")
                print("Incorrect input. Please try again ")


def create_new_contact_menu():
    logging.info('Start "create new contact" menu')
    contacts_dict = {"ID": "1", "name": "", "surname": "", "phonenumber": "", "info": ""}
    for i in contacts_dict:
        if i != "ID":
            contacts_dict[i] = new_contact_check(i)
    logging.info('Stop edit menu')
    return contacts_dict


def import_export_menu():
    logging.info('Start import/export menu')
    while True:
        print("\nImport\\Export:")
        option = input("Choose option:\n"
                       "'1'  - import file\n"
                       "'2'  - export file\n"
                       "'3'  - exit\n")
        match option:
            case "1":
                import_file(input("Input database file name: "))
                return
            case "2":
                export_file(input("Input exported file name: "))
                return
            case "3":
                logging.info('Exit from import/export menu')
                break
            case _:
                logging.warning(f"Import/export menu: wrong option selected.")
                print("Incorrect input. Please try again ")
