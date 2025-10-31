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
# len() # to get the length of string
# myString="Hello, World!"
# myString2="  Hello, World!"
# print(len(myString))
# print(len(myString2)) 
# a= "  hello world  "
# print(len(a))
# strip() # to remove whitespace from the beginning and the end of the string
# print(a.strip())
# print(a.rstrip())
# print(a.lstrip())
# b= "##hello#world!##"
# print(b.strip("#"))
# print(b.rstrip("#"))
# print(b.lstrip("#"))
# title() # to convert the first character of each word to uppercase
# a= "hello world 2d"
# print(a.title())
# # capitalize() # to convert the first character of the string to uppercase
# print(a.capitalize())
# # zfill() # to fill the string with zeros on the left side until it reaches the specified length
# num = "42"
# print(num.zfill(5))
# # upper() # to convert the string to uppercase
# print(a.upper())
# # lower() # to convert the string to lowercase
# print(a.lower())
# # end lesson 9
# start lesson 10
# string methods in python part 2
# split() # to split the string into a list of substrings based on a specified delimiter
# a= "Hello, World! Welcome to Python."
# print(a.split())
# print(a.split(","))
# b="one-two-three-four"
# print(b.split("-"))
# print(b.split("-",2)) # maxsplit
# # center() # to center the string within a specified width by adding padding characters on both sides
# c= "Hello"
# print(c.center(9)) # default padding is space
# print(c.center(9,"*"))
# # count() # to count the number of occurrences of a substring in the string
# d= "Python Programming python python"
# print(d.count("python")) # case sensitive
# print(d.count("python",0,1)) # count in specific range
# # swapcase() # to swap the case of each character in the string
# e= "Hello World"
# print(e.swapcase())
# # startswith() # to check if the string starts with a specified substring
# f= "Hello, World!"
# print(f.startswith("Hello"))
# print(f.startswith("World",3,12)) # check in specific range
# # endswith() # to check if the string ends with a specified substring
# print(f.endswith("!"))
# print(f.endswith("World",0,12)) # check in specific range
# # end lesson 10
# # start lesson 11
# # string methods in python part 3
# # index(text,start,end) # to find the index of the first occurrence of a substring in the string
# g= "Hello, World! Welcome to Python. World"
# print(g.index("W"))
# print(g.index("W",0,8)) # case sensitive
# # find(text,start,end) # to find the index of the first occurrence of a substring in the string
# print(g.find("W"))
# print(g.find("W",0,8)) # case sensitive
# # rjust and ljust() # to right justify and left justify the string within a specified width by adding padding characters
# h= "Hello"
# print(h.rjust(10))
# print(h.rjust(10,"*"))
# print(h.ljust(10))
# print(h.ljust(10,"*"))
# # splitlines() # to split the string into a list of lines
# i= "Hello World\nWelcome to Python\nEnjoy coding"
# print(i.splitlines())
# # expandtabs() # to replace tab characters with spaces
# j= "Hello\tWorld\tPython"
# print(j.expandtabs())
# print(j.expandtabs(20))
# # isTitle() # to check if the string is in title case
# k= "Hello World"
# print(k.istitle())
# l= "Hello world"
# print(l.istitle())
# # isSpace() # to check if the string contains only whitespace characters
# m= "   "
# print(m.isspace())
# n= " Hello "
# print(n.isspace())
# # isLower() # to check if the string contains only lowercase characters
# o= "hello"
# print(o.islower())
# p= "Hello"
# print(p.islower())
# # isUpper() # to check if the string contains only uppercase characters
# q= "HELLO"
# print(q.isupper())
# r= "Hello"
# print(r.isupper())
# # isIdentifier() # to check if the string is a valid identifier
# s= "HelloWorld"
# print(s.isidentifier())
# t= "Hello World"
# print(t.isidentifier())
# # isAlpha() # to check if the string contains only alphabetic characters
# u= "HelloWorld"
# print(u.isalpha())
# v= "Hello123"
# print(v.isalpha())
# # isalnum() # to check if the string contains only alphanumeric characters
# w= "Hello123"
# print(w.isalnum())
# x= "Hello 123"
# print(x.isalnum())
# # end lesson 11
# # start lesson 12
# # string methods in python part 4
# # replace(old,new,count) # to replace occurrences of a substring with a new substring
# y= "Hello World! Welcome to Python. World"
# print(y.replace("World","Universe"))
# print(y.replace("World","Universe",1)) # replace only first occurrence
# # join(iterable) # to join elements of an iterable (like list or tuple) into a single string with a specified separator
# z= ["Hello","World","Python"]
# print(" ".join(z))
# print("-".join(z))
# print(','.join(z))
# end lesson 12
# start lesson 13
# string formatting methods in python
name = "Alice"
age = 25
rank=10
print('myy name is :'+ name)
# print('my name is :' + name + 'and my age is :' + age) # TypeError: can only concatenate str (not "int") to str
# print("my name is : %s"%" haitham")
# print("my name is : %s"%" "+ name)
print("my name is : %s and my age is : %d"%(name,age))
print("my name is : %s and my age is : %d and my rank is : %f"%(name,age,rank))
# %s => string
# %d => integer
# %f => float
# control floating number of digits
print("my name is : %s and my age is : %d and my rank is : %.2f"%(name,age,rank))
# truncate string (control on string)
myLongString="Hello, World! Welcome to Python Programming."
print(" message is %.5s"% myLongString)
# end lesson 13
