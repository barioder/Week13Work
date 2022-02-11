# create a function to find the equation of 3 times 8 to the power 3
def task():
    n = 3
    x = 8
    return n*x**n


print(task())

# create a list called students_scores and find the total average for student scores
students_scores = [25, 71, 80, 50, 61]

x = len(students_scores)
sum = 0
for i in students_scores:
   sum += i
print(x)
print(sum)

average_score = sum/x
print(average_score)

# create a class called square_root to find the square root of a number
class square_root:
    def __init__(self, num):
        self.num = num
        import math
        print(math.sqrt(num))

square_root(25)


# Reversing a string is a common task during coding interviews.
# Given a string as input, output the string in reverse
value = input("Give me any string ")

value = list(value)
len = len(value)

while len > 0:
    len -= 1
    print(value[len], end='')
