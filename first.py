# lession 1
# print function in python and syntax

# print("Hello, World!");print("Hello, World!") 
# we can user ; to write multiple statements in a single line
#  print("Hello, World!") // invalid syntax indentation error
# if True:
#     print("Hello, World!")
# indentation is very important in python
# python uses indentation to define blocks of code
# in other programming languages curly braces {} are used to define blocks of code
# for example in c, c++, java
# if (true) {
#     printf("Hello, World!");
# }
# in python indentation is used to define blocks of code
# for example in python
# if True:
#     if True:
#         print("Hello, World!")
#         print("Hello, World!") 

# end lession 1
# start lesson 2
# comments in python
# single line comment
# this is a single line comment
# print("Hello, World!")  # this is also a single line comment
# multi line comment
"""
This is a multi line comment
This is also a multi line comment
"""
'''
This is another way to write multi line comment
This is also another way to write multi line comment     
'''
# end lesson 2
# start lesson 3
# some data types in python
# print (10) # integer
# print (10.5) # float
# print ("Hello, World!") # string
# print (True) # boolean
# print (None) # NoneType
# print ([1, 2, 3]) # list
# print ((1, 2, 3)) # tuple   
# print ({'a': 1, 'b': 2}) # dictionary
# print ({1, 2, 3}) # set
# end lesson 3
# start lesson 4
# variables in python
# variable declaration
# x = 10
# y = 20.5
# name = "John"
# is_student = True
# printing variables
# print (x)
# print (y)
# print (name)
# print (is_student)
# source code : original code that we write it in python (computer)
# translation : converting source code to machine code (binary code)
# machine code : code that can be understood by computer (0s and 1s)
# compilation : translate code before run time 
# interpretation : translate code at run time (fly code)
# python is an interpreted language
# run time : period App take it to executing commands
# x =10 
# x= "hello"
# print (x)
# to see the reservied words in python
# help("keywords")
# end lesson 4
# start lesson 5
#  Escape sequences in python
# \b => Backspace
# print("Hello\bWorld")  # HelloWorld
# # escape new line + black slash
# print("hello \
#       world \
#       python")
# # escape black slash
# print(" i love python \\")
# escape single quote
# print('Hello world \'test\'')
# # escape double quote
# print("Hello world \"test\"")
# line feed
# print("Hello\nWorld")
# carriage return
# print("12345\rabc")  # abcd5 it make replace for the everything after it with the same number from the start
# tab
# print("Hello\tWorld")  # Hello   World
# Hex value
# print("\x4F") # O
# end lesson 5
# start lesson 6
# Concatenation in python
# msg = "Hello"
# name = "Alice"
# print(msg+" "+name)
# a = "First \
#     Second \
#     Third"
# b= "Four \
#     Five \
#     Six "
# # print(a+" "+b)
# # print(a + "\n" + b) # with new line
# print("hello" +10)  # TypeError: can only concatenate str (not "int") to str
# end lesson 6
# start lesson 7
# String formatting in python
# name = "Alice"
# Name = 'Bob'
# mySrtingOne="This is first string 'Test'"
# mySrtingTwo='This is second string "Test"'
# print(mySrtingOne, mySrtingTwo)
# myThirdString='''\First \
# Second 
# Third 
# "test"'''
# myFourthString="""Fourth
# Fifth
# Sixth"""
# print(myThirdString)
# print(myFourthString)
# end lesson 7
# start lesson 8
# Strings-indexing and slicing in python
# 1-all data in python is object
# 2- object contain elements
# 3-every element has its own index
# 4-python user zero based indexing (index start from zero)
# 5-user squeare brackets [] to access elements by index
# 6-indexing and slicing enable accessing parts of strings,Tuples,and lists
myString="Hello, World!"
# indexing (access single item)
# print(myString[0]) # H
# print(myString[1]) # e
# print(myString[2]) # l
# print(myString[3]) # l
# print(myString[4]) # o
# print(myString[5]) # ,
# print(myString[6]) # " "
# print(myString[7]) # W
# print(myString[8]) # o
# print(myString[9]) # r
# print(myString[10]) # l
# print(myString[11]) # d
# print(myString[12]) # !
# print(myString[-1]) # !  first character from the end
# print(myString[-2]) # d  second character from the end
# print(myString[-3]) # l  third character from the end
# slicing (access multiple sequences items)
# [start:end] #end not included
# [start:end:step]
# print(myString[8:10]) #or 
# print(myString[2:4]) #ll
# # if start not exist it will be considered as 0
# print(myString[:5]) #Hello
# # if end not exist it will be considered as len(string)
# print(myString[7:]) #World!
# # get full string
# print(myString[:]) #Hello, World!
# # step
# print(myString[::2]) #Hlo ol!
# print(myString[::3]) #Hl r!
# end lesson 8
# start lesson 9
# String methods in python
myString="Hello, World!"
myString2="  Hello, World!"
print(len(myString))
print(len(myString2)) 
