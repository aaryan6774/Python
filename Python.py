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

import time
import keyword
import math
print('Hello World')
# * In other programming languages like C, C++, and Java, you will need to declare the type of variables but in Python you don’t need to do that. Just type in the variable and when values will be given to it, then it will automatically know whether the value given would be an int, float, or char or even a String.
myNumber = 3
print(myNumber)

myNumber2 = 4.5
print(myNumber2)

myNumber3 = 'HelloWorld'
print(myNumber3)

# * List is the most basic Data Structure in python. List is a mutable data structure i.e items can be added to list later after the list creation. It’s like you are going to shop at the local market and made a list of some items and later on you can add more and more items to the list.
#! # append() function is used to add data to the list.

nums = []
nums.append(21)
nums.append(40.5)
nums.append("String")
print(nums)

# Input and Output in Python
# name = input('Enter Your Name: ')
# print("Hello", name)


# num1 = int(input("ENter num1: "))
# num2 = int(input("Enter Num2: "))
# num3 = num1*num2
# print("Product is: ", num3)


number = 98
if (number >= 90):
    print("Hello")
elif number >= 10:
    print("World")
else:
    print("BoomBaam")


#    !!!! FUNCTONS !!!

# *You can think of functions like a bunch of code that is intended to do a particular task in the whole Python script. Python used the keyword ‘def’ to define a function.
# def function-name(arguments):
    # function body

def hello():
    print("Hello world")
    print("Hello Wello")


hello()


# calling function
hello()


# Python program to illustrate functions with main

def getInteger():
    # result = int(input("Enter an Integer: "))
    # return result

    # def main():
    #     print("Started")

    # calling the getInteger function and
    # storing its returned value in the output variable
    output = getInteger()
    print(output)


# now we are required to tell Python
# for 'Main' function existence
# if __name__ == "__main__":
    # main()


for step in range(5):
    print(step)


count = 0
for i in range(5):
    count = count + 1
    print(count)

#!Modules

# Python has a very rich module library that has several functions to do many tasks. You can read more about Python’s standard library by Clicking here
# ‘import’ keyword is used to import a particular module into your python code. For instance consider the following program


def main():
    num = -65
    num = math.fabs(num)
    print(num)


if __name__ == "__main__":
    main()


#! Organizations using Python :
# Google(Components of Google spider and Search   Engine)
# Yahoo(Maps)
# YouTube
# Mozilla
# Dropbox
# Microsoft
# Cisco
# Spotify
# Quora
# Facebook

# * Python 3 is a popular high-level programming language used for a wide variety of applications. Here are some basics of Python 3 that you should know


# ! Python Keywords
# and It is a logical operator


print("THe list of keywords is: ")
print(keyword.kwlist)
# ? True, False, None Keyword
# * True: This keyword is used to represent a boolean true. If a statement is true, “True” is printed.
# * False: This keyword is used to represent a boolean false. If a statement is false, “False” is printed.
# * None: This is a special constant used to denote a null value or a void. It’s important to remember, 0, any empty container(e.g. empty list) does not compute to None.

print(False == 0)
print(True == 1)

print(True + True + True)
print(True + False + False)

print(None == 0)
print(None == [])

print(True + False)
print(False + True)
print(False + False)

print(True * True)


# not: This logical operator inverts the truth value. The truth table for “not” is depicted below.
# in: This keyword is used to check if a container contains a value. This keyword is also used to loop through the container.
# is: This keyword is used to test object identity, i.e to check if both the objects take the same memory location or not.

print(True or False)
print(True and False)
print(not True)

if 'a' in 'Aaryan':
    print("a is part in Aaryan")
else:
    print("a is not a part in Aaryan")


for i in 'geeksforgeeks':
    print(i, end=" ")

print("\r")

# using is to check object identity
# string is immutable( cannot be changed once allocated)
# hence occupy same memory location
print(' ' is ' ')


# using is to check object identity
# dictionary is mutable( can be changed once allocated)
# hence occupy different memory location
print({} is {})


# * Iteration Keywords – for, while, break, continue

# for: This keyword is used to control flow and for looping.
# while: Has a similar working like “for”, used to control flow and for looping.
# break: “break” is used to control the flow of the loop. The statement is used to break out of the loop and passes the control to the statement following immediately after loop.
# continue: “continue” is also used to control the flow of code. The keyword skips the current iteration of the loop but does not end the loop.

for i in range(10):
    print(i, end=" ")

    if i == 6:
        break

print()


i = 0
while i < 10:
    if i == 6:
        i += 1
        continue
    else:
        print(i, end=" ")

    i += 1


i = 20
if i == 10:
    print('i is 10')
elif i == 20:
    print('i is 20')
else:
    print('No idea bro')


def fun():
    print("Inside a function")


fun()


def fun():
    s = 0

    for i in range(10):
        s += 1
    return s


print(fun())


def fun():
    s = 0
    for i in range(10):
        s += i
        yield s


for i in fun():
    print(i)


site = 'gfg'
if site == 'gfg':
    print("Hello gfg user")
else:
    print('Hello Other User')
print('All Set')


j = 1
while (j <= 10):
    print(j)
    j = j+1


# ?How to assign values to variables in Python and other languages

a = 1 if 20 > 10 else 0
print("The Value of a is: ", str(a))

# * Taking Input in Python
# value = input("Enter Your value: ")
# print(value)

# name = input("What is your name?")
# print(name)

# num = int(input("Enter a number: "))
# print(num)
# name = input("Enter name: ")
# print(name)
# print("Type of number: ", type(num))
# print("Type of name", type(name))


# num = int(input("Enter a number: "))
# print(num, " ", type(num))


# input1 = input()
# print(input1)

# * 1. Typecasting the input to Integer: There might be conditions when you might require integer input from the user/Console, the following code takes two input(integer/float) from the console and typecasts them to an integer then prints the sum.
# num1 = int(input())
# num2 = int(input())
# print(num1+num2)


# * 2. Typecasting the input to Float: To convert the input to float the following code will work out
# num1 = float(input())
# num2 = float(input())
# print(num1 + num2)

# * 3. Typecasting the input to String: All kinds of input can be converted to string type whether they are float or integer. We make use of keyword str for typecasting.

# string = str(input())
# print(string)
# string_default = input()
# print(string_default)


# ? Taking multiple inputs from user in Python
# * Using split() method :
# This function helps in getting multiple inputs from users. It breaks the given input by the specified separator. If a separator is not provided then any white space is a separator. Generally, users use a split() method to split a Python string but one can use it in taking multiple inputs

# x, y = int(input("Enter 2 values: ")).split()
# print("Number of boys ", x)
# print("Number of Girls: ", y)

# x, y, z = input("Enter 3 values: ").split()
# print("total number of students: ", x)
# print("Number of biys is: ", y)
# print("Number of girls: ", z)


# a, b = input("Enter 2 numbers: ").split()
# print("First number is: {} and second number is {}".format(a,b))

#! taking multiple inputs at a time
#! and type casting using list() function
# x = list(map(int, input("Enter multiple values: ").split()))
# print("List of students", x)


# * a = list(map(int, input("Emter Multiple values: ").split()))
# print(a)

# b = list(map(int, input("Enter numbers in list: ").split()))
# print(b)


#! Python program showing
#! how to take multiple input
#! using List comprehension

#! taking two input at a time
# x, y = [int(x) for x in input("Enter two values: ").split()]
# print("First Number is: ", x)
# print("Second Number is: ", y)

#! taking three input at a time
# x, y, z = [int(x) for x in input("Enter three values: ").split()]
# print("First Number is: ", x)
# print("Second Number is: ", y)
# print("Third Number is: ", z)

#! taking two inputs at a time
# x, y = [int(x) for x in input("Enter two values: ").split()]
# print("First number is {} and second number is {}".format(x, y))

#! taking multiple inputs at a time
# x = [int(x) for x in input("Enter multiple values: ").split()]
# print("Number of list is: ", x)

# taking multiple inputs at a time separated by comma
#! x = [int(x) for x in input("Enter multiple value: ").split(",")]
#! print("Number of list is: ", x)


# Python print() function prints the message to the screen or any other standard output device.

name = "John"
age = 30
print("Name: ", name)
print("Age: ", age)


# * Parameters:

# value(s): Any value, and as many as you like. Will be converted to a string before printed

# sep=’separator’ : (Optional) Specify how to separate the objects, if there is more than one.Default :’ ‘

# end=’end’: (Optional) Specify what to print at the end.Default : ‘\n’

# file : (Optional) An object with a write method. Default :sys.stdout

# # flush : (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False). Default: False


# name = "aaryan"
# age = 21
# print("Hello, my name is", name, "and I am", age, "year old.")


# * Python String Literals
# * String literals in Python’s print statement are primarily used to format or design how a specific string appears when printed using the print() function.

# * \n: This string literal is used to add a new blank line while printing a statement.
# * “”: An empty quote (“”) is used to print an empty line.

print("GFG \n is the best DSA content.")

# *The end keyword is used to specify the content that is to be printed at the end of the execution of the print() function. By default, it is set to “\n”, which leads to the change of line after the execution of print() statement.

print("GFG is best platform for DSA content")
print("GFG is the best platform for DSA content", end="**")
print("Welcome to gfg")


# count_seconds = 3
# for i in reversed(range(count_seconds + 1)):
#     if i > 0:
#         print(i, end=">>>")
#         time.sleep(1)
#     else:
#         print("Start")




# count_sec = 3
# for i in reversed(range(count_sec + 1)):
#     if i > 0:
#         print(i, end=">>>", flush=True)
#         time.sleep(1)
#     else:
#         print("Start")


# count = 60
# for i in reversed(range(count + 1)):
#     if i > 0:
#         print(i, end = ">>>")
#         time.sleep(1)
#     else:
#         print("START")


a = 12
b = 12
c = 14
print(a, b, c, sep = "-")

a = 25
b = 9
c = 2002
print(a, b, c, sep="/")

import io
dummy_file = io.StringIO()
print("Hello GFG!!", file = dummy_file)
print(dummy_file.getvalue())


print("Geeks", end = " ")
print("GEEKSforGEEKS")
a = [1,2,3,4,5]
for i in range(5):
    print(a[i], end = " ")


#* using * symbol prints the list
#* elements in a single line
l = [1,2,3,4,5,6,7,8,9]
print(*l)

l = [1,2,3,4,5,6,7,8]
for i in range(6):
    print(l[i], end = " - ")


import sys
sys.stdout.write("GFG")
sys.stdout.write("Is Best for coding! ")





