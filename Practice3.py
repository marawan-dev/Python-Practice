## Functions
# input(), optional text inside
# use help(str) for functions

#baby yoda meme
def bym():
    print('Hello there')
bym()

#simple adder
def add(x, y):
    ans = x + y
    return ans
sum = add(5,10)
print(sum)

trans_table = str.maketrans('1','2')
text = 'update 1'
result = text.translate(trans_table)
print(result)

## Lists
travel_plan = ['Russia', 'USA', 'Germany', 'Turkey']
print(travel_plan[-2])

letters = list(travel_plan[1])
print(letters)

travel_plan[-1] = 'Canada'
print(travel_plan)

del travel_plan[1]
print(travel_plan)

print('Canada' in travel_plan)

to_do = ['Study', ['Computer science', 'Math', 'Physics'], 'Pack my things']
print(to_do[1][0])

studying, material, *rest = to_do
print(studying)
print(material)
print(rest)

## lists part 2
numbers = [1,2,3,4,5]
more_numbers = [6,7,8,9]
numbers.append(more_numbers) # embeds
print(numbers)

numbers.remove(more_numbers)
numbers.extend(more_numbers) # adds
print(numbers)

numbers.insert(2,2.5)
print(numbers)

numbers.pop(2) # removes the element in the index
print(numbers)

numbers.clear()
print(numbers)

random_numbers = [11,9,3,5,43]
sorted_numbers = sorted(random_numbers) # sorted() works for both lists and tuples
print(sorted_numbers)

random_numbers.sort()
print(random_numbers)

sorted_numbers.reverse()
print(sorted_numbers)

print(sorted_numbers.index(3))

## tuples
group_names = ('Alex', 'Steve', 'Adam', 'Eve')
group_ages = (15, 17, 16, 16)
print(group_ages.count(16))

sorted_group_names = sorted(group_names, key=len)
print(sorted_group_names)
