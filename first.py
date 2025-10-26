# lession 1
# print function in python and syntax

# print("Hello, World!");print("Hello, World!") 
# we can user ; to write multiple statements in a single line
#  print("Hello, World!") // invalid syntax indentation error
if True:
    print("Hello, World!")
# indentation is very important in python
# python uses indentation to define blocks of code
# in other programming languages curly braces {} are used to define blocks of code
# for example in c, c++, java
# if (true) {
#     printf("Hello, World!");
# }
# in python indentation is used to define blocks of code
# for example in python
if True:
    if True:
        print("Hello, World!")
        print("Hello, World!") 

# end lession 1
# start lesson 2
# comments in python
# single line comment
# this is a single line comment
print("Hello, World!")  # this is also a single line comment
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
print (10) # integer
print (10.5) # float
print ("Hello, World!") # string
print (True) # boolean
print (None) # NoneType
print ([1, 2, 3]) # list
print ((1, 2, 3)) # tuple   
print ({'a': 1, 'b': 2}) # dictionary
print ({1, 2, 3}) # set
# end lesson 3
# start lesson 4
# variables in python
# variable declaration
x = 10
y = 20.5
name = "John"
is_student = True
# printing variables
print (x)
print (y)
print (name)
print (is_student)
# source code : original code that we write it in python (computer)
# translation : converting source code to machine code (binary code)
# machine code : code that can be understood by computer (0s and 1s)
# compilation : translate code before run time 
# interpretation : translate code at run time (fly code)
# python is an interpreted language
# run time : period App take it to executing commands
x =10 
x= "hello"
print (x)
# to see the reservied words in python
help("keywords")
# end lesson 4