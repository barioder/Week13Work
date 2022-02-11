# 6:40 to complete U.S 10:40
#
# 1.Create a function using the else and elif statement to get your output.

def speed(value):
    if value < 90:
        return f'{value} km/hr is not fast'

    elif value >= 90 and value <= 110:
        return f'{value} km/hr is moderate'
    else:
        return f'{value} km/hr is really a fast speed'


print(speed(120))
print(speed(90))
print('------------------------------------------------')
# 2.Create a nesting dictionary.
students = {'Steve': {'class': 'P5', 'Sport': 'Soccer', 'Age': 10},
            'Alex': {'class': 'P2', 'Sport': 'Running', 'Age': 7},
            'Tim': {'class': 'P7', 'Sport': 'Rugby', 'Age': 12}}

print(students)
print('------------------------------------------------')
# 3.Create a while loop that prints only odd numbers.
n = 0

while n < 20:
    if n % 2 == 1:
        print(n)

    n += 1

print('------------------------------------------------')
# 4.You need to make a function that converts a foot value to inches.
# (1 foot has 12 inches). Define convert() function, that takes the foot value
# as an argument and outputs the inches.


def convert(foot_value):
    return f'The foot value in inches is {foot_value * 12}'


print(convert(4))

print('------------------------------------------------')
# 5. Create a list and and find out the length of that list.

list1 = [1, 2, 3, 4, 5, 6]

print('Length of the list is ', len(list1))
