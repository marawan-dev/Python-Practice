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

## sets
prime = {2, 3, 5, 7, 11, 13}
print(prime)

prime.add(0)
print(prime)

# .discard() works too
prime.remove(0)
print(prime)

even = {2, 4, 6, 8 , 10, 12}
odd = {1, 3, 5, 7, 9, 11}
my_nums = {2, 3}

print(prime.issubset(odd))
print(prime.issuperset(my_nums))

print(prime.isdisjoint(even))

# union
print(even | odd)

# intersection
print(odd & prime)

# difference
print(odd - prime)

# symmetric difference
print(odd ^ prime)

## Modules
import math as m
# from (modules) import '', '' also works
print(m.sqrt(25))

## Certification project
test_settings = {
    'sound': 70,
    'screen_Brightness': 90,
    'battery_Life': 21,
    'wifi': 'online',
    'camera': 'off'
}

pass_setting = ('Privacy', 'Hidden')

hacker = ('Camera', 'On')

def add_setting(dictionary, tuple_dict):
    key, value = tuple_dict
    key = key.lower()
    value = value.lower()

    if key in dictionary:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        tuple_dict = key, value
        dictionary[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

print(add_setting({'theme': 'light'}, ('volume', 'high')))

def update_setting(dictionary, tuple_dict):
    key, value = tuple_dict
    key = key.lower()
    value = value.lower()
    if key in dictionary:
        dictionary[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

print(update_setting({'theme': 'light'}, ('volume', 'high')))

def delete_setting(dictionary, key):
    key = key.lower()
    if key in dictionary:
        del dictionary[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return 'Setting not found!'

print(delete_setting({'theme': 'light'}, 'theme'))

def view_settings(dictionary):
    if dictionary == {}:
        return 'No settings available.'
    else:
        settings_list = ''
        for setting, option in dictionary.items():
            setting = str(setting).capitalize()
            settings_list += setting + ': '
            settings_list += option + '\n'
        return f"Current User Settings:\n{settings_list}"
print(view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}))