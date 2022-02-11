# 1.Create a dictionary and pop and element out of your dictionary
# and then update it.
students = {'Derrick': 70,
            'Timothy': 85,
            'Steven': 71,
            'Maria': 89}

students.pop('Derrick')
print(students)

students.update({'Derro': 72})
print(students)


print('-------------------------------------------------------')
# 2.Create a function implementing conditional statement to return and output of true or false.


def compare(value1, value2):
    if value1 > value2:
        print(True)
    else:
        print(False)


compare(5, 7)


print('---------------------------------------')
# 3.Create a function that takes a user input.


def person(name):
    print('Hey', name, '\nNice name')


person(input('What is your name? '))

print('---------------------------------------')
# 4.Create 2 lists and merge them together to make it 1 list.
list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
merge = list_1 + list_2
print(merge)