# del is to delete a variable
# = is to set a variable
# != is not equal, == is equal
#break after and if will stop the loop
def protocal(name):
    print("welcome", name)
def exam_mark(mark): 
    if mark <= 60:
        print("Better luck next time")
    elif mark <= 70:
        print("Could have been worse")
    elif mark <= 80:
        print("Good work")
    else:
        print("Great job")
def age_calc(year,now_year):
    age = now_year - year
    return age

#counting to ten
x=0
while(x<=5):
    print(x)
    x=x+1
for x in range(5,11):
    print(x)

#days of the week
days=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
for day in days:
    if(day=="Wed"):continue
    print(day)

import math
print(math.pi)

#var = range(int) used for loops
#isinstance(var_1,var_2) checks if both are the same
# / is for "''"