import sys
import io
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
print(a, b, c, sep="-")

a = 25
b = 9
c = 2002
print(a, b, c, sep="/")

dummy_file = io.StringIO()
print("Hello GFG!!", file=dummy_file)
print(dummy_file.getvalue())


print("Geeks", end=" ")
print("GEEKSforGEEKS")
a = [1, 2, 3, 4, 5]
for i in range(5):
    print(a[i], end=" ")


# * using * symbol prints the list
# * elements in a single line
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(*l)

l = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(6):
    print(l[i], end=" - ")


sys.stdout.write("GFG")
sys.stdout.write("Is Best for coding! ")


# Python end parameter in print()
print("Welcome TO", end=" ")
print("GeeksForGeeks", end=" ")

print("Python", end='@')
print("GeeksForGeeks")

print('G', 'F', sep="", end="")
print("G")
print('09', '12', '2016', sep='-', end="\n")
print('Red', 'Green', 'Blue', sep=",", end='@')
print('geeksForgeeks')

# ? Using end to concatenate strings:
# In this example, we use the end parameter to concatenate the two print() statements into a single line of output. The end parameter is set to a space character ” ” for the first print() statement, so the second print() statement will start on the same line, separated by a space character.
# The end parameter is a useful feature of the print() function in Python that can be used to control the formatting of output in various ways.

name = "Alice"
age = 30
print("My name is ", name, "and I am", age, "Year of age", end=" ")
print("Nice to meet you!!!")


# ? sep parameter in print()
print('G', 'F', 'G', sep="")
print('09', '12', '2016', sep="-")
print('Aaryan', 'GFG', sep='@')

print('G', 'F', sep='', end='')
print('G')
print('25', '09', '2002', sep='-', end='\n')
print('Aaryan', 'Vasalya', sep='', end='@')
print('GFG')
# -----------------------------------
# ! import antigravity
# -----------------------------------
print('Apple', 'Oranges', 'Bananas', sep=',')
print('One', 'Two', 'Three', sep=';')
print('?????', '?????', '?????', sep='????')


# * Formatting Output using String Modulo Operator(%)
# The Modulo % operator can also be used for string formatting. It interprets the left argument much like a printf()-style format as in C language strings to be applied to the right argument. In Python, there is no printf() function but the functionality of the ancient printf is contained in Python. To this purpose, the modulo operator % is overloaded by the string class to perform string formatting. Therefore, it is often called a string modulo (or sometimes even called modulus) operator. The string modulo operator ( % ) is still available in Python(3.x) and is widely used. But nowadays the old style of formatting is removed from the language.

print("Geeks: %2d, Portal: %5.2f" % (1, 05.333))


print('I love {} for "{}!"'.format('Geeks', 'Geeks'))
print('{0} and {1}'.format('Geeks', 'Portal'))
print('{1} and {0}'.format('Geeks', "Geeks"))
print('{} Hello to this {} world'.format("Say", 'Beautiful'))

# The brackets and characters within them (called format fields) are replaced with the objects passed into the format() method. A number in the brackets can be used to refer to the position of the object passed into the format() method.

print('Number one portal is {0}, {1}, and {other}'.format(
    'Geeks', 'for', other='Geeks'))

#! print("Geeks: {0:2d}, Portal: {1:8:2f}".format(12, 00.546))
# Changing positional argument
# !print("Second argument: {1:3d}, first one: {0:7.2f}".
# !      format(47.42, 11))

# !print("Geeks: {a:5d},  Portal: {p:8.2f}".
# !     format(a = 453, p = 59.058))

# In Python programming, Operators in general are used to perform operations on values and variables. These are standard symbols used for the purpose of logical and arithmetic operations. In this article, we will look into different types of Python operators.

# !Integer division( Floor division)
#! The quotient returned by this operator is dependent on the argument being passed. If any of the numbers is float, it returns output in float. It is also known as Floor division because, if any number is negative, then the output will be floored

print(10//3)
print(-5//3)
print(5.0//2)
print(-5//1)

# * Precedence of Arithmetic Operators in Python
# The precedence of Arithmetic Operators in python is as follows:

# P – Parentheses
# E – Exponentiation
# M – Multiplication (Multiplication and division have the same precedence)
# D – Division
# A – Addition (Addition and subtraction have the same precedence)
# S – Subtraction
# * The modulus operator helps us extract the last digit/s of a number. For example:
# ?x % 10 -> yields the last digit
# ?x % 100 -> yield last two digits

a = 9
b = 4
add = a + b
sub = a - b
mul = a * b
mod = a % b
p = a**b
f = a//b
print(sub)
print(sum)
print(mul)
print(mod)
print(p)
print(f)

a = 13
b = 33
print(a > b)
print(a < b)
print(a == b)
print(a >= b)
print(a <= b)


# * Precedence of Logical Operators in Python
# The precedence of Logical Operators in python is as follows:

# Logical not
# logical and
# logical or


a = True
b = False
print(a and b)
print(a or b)
print(not a, not b)


print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

a = 10
b = a
print(b)
b += a
print(b)
b *= a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)


#? Identity Operators in Python
# In Python, is and is not are the identity operators both are used to check if two values are located on the same part of the memory. Two variables that are equal do not imply that they are identical. 

# is          True if the operands are identical 
# is not      True if the operands are not identical 

a = 10
b = 20
c = a
print(a is not b)
print(a is b)
print(a is c)


#? Membership Operators in Python
# In Python, in and not in are the membership operators that are used to test whether a value or variable is in a sequence.

# in            True if value is found in the sequence
# not in        True if value is not found in the sequence


x = 24
y = 20
list = [10, 20, 23, 30, 78]
if x not in list:
    print("No No No")
else:
    print("X in list")

if y in list:
    print("Noooo diabito Roll Back to kitchen")
else: 
    print("Y is not in list")


#? Ternary Operator in Python
# in Python, Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5. 

# It simply allows testing a condition in a single line replacing the multiline if-else making the code compact.

a, b = 10, 20
min = a if a < b else b
print(min)


print(9//2)

# i = 0
# while i < 3:
#     print i
#     i++
#     print(i+1)
