print('Hello World')
print('Twinklw, twinkle, little star, \n \t How I wonder what you are! \n \t \tUp above the world so high, \n \t \t like a diamod in the sky. \n Twinkle, twinkle, little star, \n \t How I womder what you are!')

x,y,z = (1,2,3,4,5,6,7)[1::2]
print(y)
a = 3
b = -3
a, b = (b,a)[::-1]
print(a)
print(b)
# sys.version(0)
# open cmd and type python --version
# #*
# #!
# #?
# #
import datetime
now = datetime.datetime.now()
print(now)
# #! now = datetime._Time.now()
# #! print(now)
# #? Radius of Circle
r = float(input('Enter Radius of circle: '))
print("Area of Circle is: " + str(3.14*r*r))
# #? Area of Rectangle: 
length = float(input('Enter Length of rectangle:  '))
breadth = float(input('Enter Breadth of rectangle: '))
print('Area of rectangle is: ' + str(length*bredth) + " cm square")
# ? 5. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
first_name = str(input('Enter Your First Name: '))
second_name = str(input('Enter your second name: '))
print('Your name in reversed: ' + str(second_name ) + str(first_name))
# ? 6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# ? guessing a random number
r_nun = 9
num = int(input('Enter a Number from 1-10'))
if num == r_nun:
    print('You got it right)
else:
    print('Try 1 more time')
# ? Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
values = input('Enter some values')
list = values.split(',')
print(list)
tuple = tuple(values)
print(tuple)
# ?!Write a Python program that accepts a filename from the user and prints the extension of the file.
# ! file_name = input('Enter a file name')
# ! print(file_name)
# ! f_extns = file_name
# ?Write a Python program to display the first and last colors from the following list.
color_list = ["Red", "Green", "White", "Black"]
color_list = ["red", "green", "blue"]
print((color_list[0], color_list[2]))
color_input = input('Enter Color in this list')
list = color_input.split(',')
print(list)
#  Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_date = (11,12,2014)
print('The examination will start from:%i / %i / %i '%exam_date)
# The placeholders %i are used to format the integers.
#  ? Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# ?Sample value of n is 5
#? Expected Result: 615
# ! typecasting?
a = int(input('Enter a number'))
n1 = int("%s"%a)
n2 = int("%s%s"%(a, a))
n3 = int("%s%s%s"%(a, a, a))
print(n1+n2+n3)
#* %s specifically is used to perform the concatenation of strings together. It allows us to format a value inside a string. It is used to incorporate another string within a string. It automatically provides type conversion from value to string.


ASSIGNMENT 2
