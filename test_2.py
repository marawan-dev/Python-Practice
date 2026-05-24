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

print('Calculations:')

int_1 = 24
int_2 = 5

# the % is the mod
remainder = int_1 % int_2

# floor division is //
years = int_1 // int_2

# Exponentiation is **
rate = int_1 ** int_2

print(remainder, type(remainder))
print(years)
print(rate)

remainder = float(remainder)
print(type(remainder))
# int does the same thing

float_1 = 8.3
float_2 = -2.1

multiply_float = float_1 * float_2
print(round(abs(multiply_float), 2))
# round(var, d.p.)

#combined function pow(base, power, mod)
print(pow(2,3,5))
print(pow(2,3))

#argumented operations
int_1 += int_2
print(int_1)
int_2 -= int_1
print(int_2)

#text operations
intro1 = 'Hello '
intro2 = 'Internet'
# *= repeats the text
intro1 *= 2
intro1 += intro2
print(intro1)

