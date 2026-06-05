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