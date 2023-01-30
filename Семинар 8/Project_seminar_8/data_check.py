from logg import logging


def find_existing_contact(request, contact_info):
    logging.info(f"Search for {request} in data base")
    contacts = [" ".join(i.values()) for i in contact_info if request in i.values()]
    if contacts:
        logging.info(f"Search result: {contacts}")
        print(*contacts, sep="\n", end="\n\n")
        return [n[0] for n in contacts]
    else:
        logging.warning(f"Request not found: {request}")
        print("Request not found.\n")
        return 0


def duplication_check(new_contact: dict, contact_info):
    contact = list(new_contact.values())[1:]
    all_contacts = [list(k.values())[1:] for k in contact_info]
    return contact not in all_contacts


def new_contact_check(number):
    user_input = input(f"Input {number}: ")
    while True:
        if number in "name surname info":
            if user_input.isalpha():
                break
        if number == "phone number":
            if user_input.isdigit() and len(user_input) == 11:
                break
        user_input = input(f"Incorrect input!\n"
                           f"Input {number}: ")
    return user_input
