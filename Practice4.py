## Dictionaries
archive = {
    'email': 'Marwan123',
    'minecraft': 'rangerstech',
}
print(archive['email'])

archive['whatsapp'] = '9564-2431'
print(archive['whatsapp'])

# if key is not in the dictionary, second parameter will be printed
print(archive.get('Visa', 'N/A'))

# items() = keys() + values()

# popitem() removes the last added item
archive.pop('minecraft')

archive.update({'whatsapp': 92761323})
print(archive.items())

## looping dictionaries
menu = {
    'Ice cream': 4,
    'Latte': 9,
    'Cookie': 10,
    'Cheese cake': 15
}

for food, price in menu.items():
    price = price * .8
    menu[food] = price
print(menu)