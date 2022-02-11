import math
print(math.pow(2,6))

name = "Codeit"

for i in name:
        print(i)

print("Hello/nWorld")

x = 10

if x >= 11:
    print("True")

else:
    print("False")


print("Hello\tWorld")

bio = {"Name": "Jack","Email": "shawnday.dl@gmail.com", "Number": 12014824388}

print(bio.values())

y = 5
x = 7

print(y <= x and y != x)


for i in range(1,5,2):
    print(i)

bio = {"Name": "Jack","Email": "shawnday.dl@gmail.com", "Number": 12014824388}

print(bio)

alist = [10, 20, 30, 40]

print(alist[2])

x,y,z = 1,2,3

print(y*z*x)

# You're making a calculator that should add multiple numbers taken from input
# and output the result. The number of inputs is variable and should stop when the user enters "stop"
input_values = []
while True:
    value = input('Please Enter a number')

    if value != 'stop':
        input_values.append(int(value))
    if value == 'stop':
        print('The sum of the numbers you entered is', sum(input_values))
        break




# The given outputs A B C D (each letter is separated by a space).
# Modify the code to output each letter on a separate line, resulting in the following output.


data = 'A B C D'

for letter in data:
    if letter != ' ':
        print(letter)

# You are given a program with two inputs: one as password and the second one as
# password repeat. "Complete" if password and repeat are equal, and output "wrong", if they are not.

password = '123@Badx'
password_repeat = '123Badx'

if password == password_repeat:
    print('Complete')

else:
    print('Wrong')

# create a file called answersheet.txt and write your answers on that sheet.

f = open("answersheet.txt", "w")
f.write("My answers go here")
f.close()