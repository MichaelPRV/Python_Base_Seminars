# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, 
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

def alphabetical_index(colleagues):
    dictionary = {}

    for name in colleagues:
        key = name[0].upper()
        if key not in dictionary:
            dictionary[key] = []
        dictionary[key].append(name)

    return dict(sorted(dictionary.items()))


employee = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]

print(alphabetical_index(employee))
