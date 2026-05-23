first_name = 'Marawan'
last_name = 'Rageb'
print('M' in first_name,'raw' in first_name,'s' in first_name)

#print(len(first_name)) gives length of string

print(first_name[4],first_name[1],first_name[2],first_name[6])
full_name = first_name + ' ' + last_name
code = 2671
student_id = full_name + ' ' + str(code)
print(student_id)

plane = 'Boeing'
model = 747
plane_id = plane
plane_id += str(model)
print(plane_id)
boarding = f'Hello {full_name}, you are on the {plane_id}'
print(boarding)

#slicing - string[start:end:step]
print(boarding[21:24])
print(full_name[::-1].upper())
#.lower() does the opposite

#.split turns strings into sets
unstriped = ' oak wood '
wood_1 = unstriped.strip()
wood_2 = wood_1.replace('oak', 'spruce')

print(wood_1,'and', wood_2)

craft = ['stone','pickaxe']
print(craft)
print(' '.join(craft))

print(boarding.startswith('Hello'))
#same with .endswith()

#substring index search, returns -1 of nothing found
print(boarding.find('on'))

#number of times a substring was used
print(boarding.count('e'))

#.capitalize() just makes the first index capital
#.title() capitalizies the first letter of each word
#.isupper(), returns true if all letters are lowercase