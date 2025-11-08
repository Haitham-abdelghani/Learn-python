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
# name = "Alice"
# age = 25
# rank=10
# print('myy name is :'+ name)
# # print('my name is :' + name + 'and my age is :' + age) # TypeError: can only concatenate str (not "int") to str
# # print("my name is : %s"%" haitham")
# # print("my name is : %s"%" "+ name)
# print("my name is : %s and my age is : %d"%(name,age))
# print("my name is : %s and my age is : %d and my rank is : %f"%(name,age,rank))
# # %s => string
# # %d => integer
# # %f => float
# # control floating number of digits
# print("my name is : %s and my age is : %d and my rank is : %.2f"%(name,age,rank))
# # truncate string (control on string)
# myLongString="Hello, World! Welcome to Python Programming."
# print(" message is %.5s"% myLongString)
# end lesson 13
# start lesson 14
# advanced string formatting in python
# name = "Alice"
# age = 25
# rank=10.56789
# print("my name is : {}".format(name))
# print("my name is : {} and my age is : {}".format(name,age))
# print("my name is : {:s} and my age is : {:d} and my rank is : {:f}".format(name,age,rank))
# print("my name is : {:s} and my age is : {:d} and my rank is : {:.2f}".format(name,age,rank))
# print("my name is : %s and my age is : %d and my work is : %f" % (name,age,rank))
# print("my name is : {} and my age is : {} and my work is : {}" .format (name,age,rank))
# myMoney=1234567890
# print("my money is : {}".format(myMoney))
# print("my money is : {:,d}".format(myMoney))
# # rearrange items
# a,b,c= "one","two","three"
# print("first : {1} {2} {0}".format(a,b,c)) #indexing
# format in version 3.6+
# name = "Alice"
# age = 25
# print("my name is :{name} and my age is : {age}")
# print(f"my name is : {name} and my age is : {age}")
# end lesson 14
# start lesson 15
# number systems in python
# decimal (base 10)
# print(10)
# # binary (base 2)
# print(0b1010)
# print(type(10))
# print(type(0b1010))
# # complex 
# myStringComplex=3 + 5j
# print(3 + 5j)
# print(type(3 + 5j))
# print("real part is : {}".format(myStringComplex.real))
# print("imaginary part is : {}".format(myStringComplex.imag))
# # you can convert from Int to float or complex
# myInt=10
# print(myInt)
# myInt=float(myInt)
# print(myInt)
# myInt=complex(myInt)
# print(myInt)
# myInt=int(myInt)
# print(myInt) #int() argument must be a string, a bytes-like object or a real number, not 'complex'
# end lesson 15
# start lesson 16
#  arithmetic operators in python
# addition +
# print(10+20)
# print("Hello " + "World")
# print(-10 +20)
# # subtraction -
# print(20-10)
# print(-10 - -20)
# # multiplication *
# print(10*2)
# print("Hello " * 3)
# print(-5 * 4)
# # division /
# print(20/5)
# print(-20/5)
# print(7/3)
# # floor division //
# print(20//3)
# print(-20//3)
# print(20.5//3)
# print(110//5) #
# # modulus %
# print(20%3)
# print(-20%3)
# print(20%-3)
# print(8 % 2)
# print(7 % 2)
# print(13 % 2)
# print(22 % 5)
# # exponentiation **
# print(2**3)
# print(5**4)
# print(9**0.5)
# print(27**(1/3))
# end lesson 16
# start lesson 17
# Lists
# 1- list is a collection which is ordered and changeable
# 2- list allows duplicate members
# 3- list is defined by square brackets []
# 4- list can contain different data types
# 5- list can be nested (a list can contain another list)
# 6- list support indexing and slicing
# 7- list support many built-in methods
# 8- list is mutable (can be changed) ==> add,remove,update elements
# 9- list can be iterated using loops

# myList = ["one", "two", "three", 4, 5.55, True, [6, 7, 8]]
# print(myList)
# print(type(myList))
# print(len(myList))
# print(myList[0])  # first element
# print(myList[6])  # nested list
# print(myList[6][1])  # access element from nested list
# print(myList[-1])  # last element
# print(myList[1:4])  # slicing
# print(myList[0:]) # from start to end
# print(myList[:3])  # from start to index 2
# print(myList[::2])  # slicing with step
# myList[0] = "ONE"  # update element
# print(myList)
# myList[0:4] = ["First", "Second", "Third", "Fourth"]  # update multiple elements
# print(myList)
# # append() # to add an element at the end of the list
# myList.append("new item")
# print(myList)
# newList = [9, 10, 11]
# myList.append(newList)  # add nested list
# print(myList)
# print(myList[8][0])
# # extend() # to add multiple elements at the end of the list
# myList.extend([12, 13, 14])
# print(myList)
# remove() # to remove an element from the list
# a= [1, 2, 3, 4, 3];
# a.remove(3)
# print(a)
# # sort() # to sort the list in ascending order
# b= [5, 2, 9, 1, 5, 6]
# b.sort()
# print(b)
# b.sort(reverse=True)
# print(b)
# b.sort(reverse=False)
# print(b)
# # reverse() # to reverse the order of the list
# c= [1, 2, 3, 4, 5,"one","two","three"]
# c.reverse()
# print(c)
# end lesson 17
# start lesson 18
# list methods in python part 2
# clear() # to remove all elements from the list
# myList = [1, 2, 3, 4, 5]
# myList.clear()
# print(myList)
# # copy() # to create a shallow copy of the list
# originalList = [1, 2, 3, 4, 5]
# copiedList = originalList.copy()
# print(copiedList)
# originalList.append(6)
# print(copiedList)
# # count() # to count the occurrences of an element in the list
# myList = [1, 2, 3, 2, 4, 2, 5]
# print(myList.count(2))
# # index() # to find the index of the first occurrence of an element in the list
# myList = ['a', 'b', 'c', 'd', 'b']
# print(myList.index('b'))
# # insert() # to insert an element at a specific index in the list
# myList = [1, 2, 4, 5]
# myList.insert(2, 3)  # insert 3 at index 2
# print(myList)
# # pop() # to remove and return an element at a specific index in the list
# myList = [1, 2, 3, 4, 5]
# removedElement = myList.pop(2)  # remove element at index 2
# print(removedElement)
# print(myList)
# end lesson 18
# start lesson 19
# Tuples in python
# 1- tuple is a collection which is ordered and unchangeable
# 2- tuple allows duplicate members
# 3- tuple is defined by parentheses ()
# 4- tuple can contain different data types
# 5- tuple can be nested (a tuple can contain another tuple)
# 6- tuple support indexing and slicing
# 7- tuple support many built-in methods
# 8- tuple is immutable (cannot be changed)
# myTuple = ("one", "two", "three", 4, 5.55, True, (6, 7, 8))
# myTupleTwo = 1, 2, 3, 4  # without parentheses
# print(myTuple)
# print(type(myTuple))
# print(myTupleTwo)
# print(type(myTupleTwo))
# print(len(myTuple))
# print(myTuple[0])  # first element
# print(myTuple[6])  # nested tuple
# myTupleTwo[0] = 10  # TypeError: 'tuple' object does not support item assignment
# tuple with single element
# mySingleTuple = (5,)
# print(type(mySingleTuple))
# # tuple concatenation
# myTupleA = (1, 2, 3)
# myTupleB = (4, 5, 6)
# myTupleC = myTupleA + myTupleB
# print(myTupleC)
# # tuple repetition , list repetition , string repetition
# myNewTuple = myTupleA * 3
# myNewString = "Hello " * 3
# myNewList = [1, 2, 3] * 3
# print(myNewTuple)
# print(myNewString)
# print(myNewList)
# a= (1, 2, 3, 4, 3)
# print(a.count(3))
# b= ('a', 'b', 'c', 'd', 'b')
# print("The position is : {:d}".format(b.index('b')))
# # tuple dustruction
# myTuple = (10, 20, 30)
# a, b, c = myTuple
# print(a)
# print(b)
# print(c)
# end lesson 19
# start lesson 20
# set in python
# 1- set is a collection which is unordered and unindexed
# 2- set is mutable (can be changed) but elements are immutable
# 3- set does not allow duplicate members
# 4- set is defined by curly braces {} or by the set() function
# 5- set can contain different data types
# 6- set cannot be accessed by index or slicing
# 7- set support many built-in methods
# 8- cant make indexing or slicing
# mySet = {1, 2, 3, 4, 5}
# # print(mySet[0]) # TypeError: 'set' object is not subscriptable
# # print(mySet[0:2]) # TypeError: 'set' object is not subscriptable
# # print(type(mySet))
# mySetTwo = {"apple", "banana", "cherry", 1, 2.5, True}
# print(mySetTwo)
# # mySetThree = {"orange", "grape", "watermelon", 3, 4.5, False,[5,6]} # TypeError: unhashable type: 'list'
# mySetFour = {"orange", "grape", "watermelon", 3, 4.5, False,(5,6)}  # tuple is immutable
# # items is unique
# mySetFive = {1, 2, 2, 3, 4, 4, 5}
# print(mySetFive)  # {1, 2, 3, 4, 5}
# set methods
# clear() # to remove all elements from the set
# mySet = {1, 2, 3, 4, 5}
# mySet.clear()
# print(mySet)
# # union() # to combine two sets and return a new set with all unique elements from both sets
# setA = {1, 2, 3}
# setB = {3, 4, 5}
# setC = setA.union(setB)
# print(setC)
# # using | operator
# setD = setA | setB
# print(setD)
# print(setA.union(setB,{6,7,8})) 
# add() # to add an element to the set
mySet = {1, 2, 3}
# mySet.add(4)
# print(mySet)
# # copy() # to create a shallow copy of the set
# originalSet = {1, 2, 3}
# copiedSet = originalSet.copy()
# print(copiedSet)
# originalSet.add(4)
# print(copiedSet)
# # remove() # to remove an element from the set
# mySet.remove(2)
# print(mySet)
# mySet.remove(100)  # KeyError: 100
# discard() # to remove an element from the set if it exists
# mySet.discard(3)
# print(mySet)
# mySet.discard(100)  # no error
# print(mySet)
# pop() # to remove and return an arbitrary element from the set
# removedElement = mySet.pop()
# print(removedElement)
# print(mySet)
# # update() # to add multiple elements to the set
# mySet.update([4, 5, 2])
# print(mySet)
# end lesson 20
# start lesson 21
# set methods in python part 2
# difference() # to return a new set with elements in the first set that are not in the second set
# setA = {1, 2, 3, 4, 5}
# setB = {4, 5, 6, 7, 8}
# print(setA.difference(setB))  # {1, 2, 3}
# # using - operator
# print(setA - setB)  # {1, 2, 3}
# # difference_update() # to remove elements from the first set that are also in the second set and update the first set
# a={1,2,3,4}
# b={3,4,5,6}
# a.difference_update(b)
# print(a)  # {1, 2}
# # using -= operator
# a={1,2,3,4}
# b={3,4,5,6}
# a -=b
# print(a)  # {1, 2}
# intersection() # to return a new set with elements that are common to both sets
# a={1,2,3,4}
# b={4,5,6,7}
# setC = a.intersection(b)
# print(setC)  # {4}
# # using & operator
# setD = a & b
# print(setD)  # {4}
# # intersection_update() # to update the first set with elements that are common to both sets
# a={1,2,3,4}
# b={4,5,6,7}
# a.intersection_update(b)
# print(a)  # {4}
# # using &= operator
# a={1,2,3,4}
# b={4,5,6,7}
# a &= b
# print(a)  # {4}
# # symmetric_difference() # to return a new set with elements in either set but not in both
# a={1,2,3,4}
# b={4,5,6,7}
# setC = a.symmetric_difference(b)
# print(setC)  # {1, 2, 3, 5, 6, 7}
# print(a)
# # using ^ operator
# setD = a ^ b
# print(setD)  # {1, 2, 3, 5, 6, 7}
# # symmetric_difference_update() # to update the first set with elements in either set but not in both
# a={1,2,3,4}
# b={4,5,6,7}
# a.symmetric_difference_update(b)
# print(a)  # {1, 2, 3, 5, 6, 7}
# # using ^= operator
# a={1,2,3,4}
# b={4,5,6,7}
# a ^=b
# print(a)
# # end lesson 21
# # start lesson 22
# # set methods in python part 3
# # issuperset() # to check if the first set is a superset of the second set
# a={1,2,3,4,5} 
# b={2,3}
# print(a.issuperset(b))  # True => we check if the {2,3} exsisting in the set a or not
# print(b.issuperset(a))  # False => we check if the {1,2,3,4,5} exsisting in the set b or not
# # issubset() # to check if the first set is a subset of the second set
# a={1,2,3}
# b={1,2,3,4,5}
# print(a.issubset(b))  # True => we check if the {1,2,3} exsisting in the set b or not
# print(b.issubset(a))  # False => we check if the {1,2,3,4,5} exsisting in the set a or not
# # isdisjoint() # to check if two sets have no elements in common
# a={1,2,3}
# b={4,5,6}
# print(a.isdisjoint(b))  # True => no common elements
# c={3,4,5}
# print(a.isdisjoint(c))  # False => common element is 3
# # end lesson 22
# # start lesson 23
# # dictionary in python
# # 1-dictionary items are enclosed in curly braces {}
# # 2-dictionary items are key:value pairs
# # 3-dictionary key need to be Immutable => (Number, String ,Tuple) List not allowed
# # 4-dictionary value can be anytype data type
# # 5-dictionary key must be unique
# # 6-dictionary is unordered (python 3.7+ ordered)
# # 7-dictionary is mutable (can be changed)
# user={
#     "name":"Alice",
#     "age":25,
#     "is_student":True,
#     "courses":["Math","Science","History"],
#     "address":{
#         "street":"123 Main St",
#         "city":"New York",
#         "zip":"10001"
#     },
#     (1,2,3):"set as a key",  # valid but not recommended
#     "name":"Bob"  # duplicate key, the last one will be used
# }
# print(user)
# print(type(user))
# print(len(user))
# print(user["name"])  # access value by key
# print(user["address"]["city"])  # access nested dictionary value
# print(user[(1,2,3)])  # access value by tuple key
# print(user.get("age"))  # access value using get() method
# print(user.keys())
# print(user.values())
# # Two-dimensional dictionary
# students={
#     "student1":{
#         "name":"Alice",
#         "age":20
#     },
#     "student2":{
#         "name":"Bob",
#         "age":22
#     },
#     "student3":{
#         "name":"Charlie",
#         "age":21
#     }
# }
# print(students)
# print(students["student2"]["name"])
# # create dictionary from variables
# frameWorkOne={
#     "name":"Django",
#     "language":"Python",
#     "version":3.2
# }
# allFrameworkName={
#     "one":frameWorkOne["name"],
#     "two":frameWorkOne["language"],
#     "three":frameWorkOne["version"],
#     "four":frameWorkOne
# }
# print(allFrameworkName)
# end lesson 23
# start lesson 24
# dictionary methods in python
# # clear() # to remove all items from the dictionary
# myDict={
#     "name":"Alice",
#     "age":25,
#     "is_student":True
# }
# myDict.clear()
# print(myDict)  # {}
# # update() # to update the dictionary with new key-value pairs or modify existing ones
# myDict={
#     "name":"Alice",
#     "age":25,
#     "is_student":True
# }
# myDict['name']='bob'  # update existing key
# print(myDict)
# myDict.update({"age":30,"city":"New York"})  # update existing key and add new key
# print(myDict)
# copy() # to create a shallow copy of the dictionary
# originalDict={
#     "name":"Alice",
#     "age":25,
#     "is_student":True
# }
# copiedDict=originalDict.copy()
# print(copiedDict)
# originalDict["age"]=30
# print(copiedDict)
# print(originalDict)
# # keys() # to get a view object of all keys in the dictionary
# print(originalDict.keys())
# # values() # to get a view object of all values in the dictionary
# print(originalDict.values())
# setdefault() # to get the value of a key if it exists, otherwise set it to a default value
# myDict={
#     "name":"Alice",
#     "age":25
# }
# print(myDict.setdefault("name","Bob"))  # Alice
# print(myDict.setdefault("age"))  # New York
# print(myDict.setdefault("city","New York"))  # New York
# print(myDict)
# popitem() # to remove and return an arbitrary key-value pair from the dictionary

# myDict={
#     "name":"Alice",
#     "age":25
# }
# myDict.update({"city":"New York"})
# print(myDict)
# print(myDict.popitem())
# # items() # to get a view object of all key-value pairs in the dictionary
# print(myDict.items())
# myDict.update({"country":"USA"})
# print(myDict.items())
# # fromkeys() # to create a new dictionary with keys from an iterable and values set to a specified value
# keys = ["name", "age", "city"]
# defaultValue = "Unknown"
# newDict = dict.fromkeys(keys, defaultValue)
# print(newDict)
# end lesson 24
# start lesson 25
# Boolean in python
# 1- boolean data type has two values: True and False
# 2- boolean values are often used in conditional statements and comparisons
# 3- boolean values can be the result of comparison operators
# 4- boolean values can be converted to integers (True=1, False=0) and vice versa
# 5- boolean values can be combined using logical operators (and, or, not)
# 6- boolean values can be used in control flow statements (if, while, for)
# is_raining = True
# is_sunny = False
# print(is_raining)
# print(is_sunny)
# bool() # to convert a value to boolean
# print(bool(1))  # True
# print(bool(0))  # False
# print(bool(""))  # False
# print(bool("Hello"))  # True
# print(bool([]))  # False
# print(bool([1, 2, 3]))  # True
# # boolean operators
# # and , or , not
# age = 20
# country = "USA"
# print(age >= 18)  # True
# print(country == "USA")  # True
# print(age>=18 and country=="USA")  # True
# print(age<18 or country=="USA")  # True
# print(not(age>=18))  # False
# print(not(country=="USA"))  # False
# print(age<18 or country!="USA")  # False
# end lesson 25
# start lesson 26
# assignment operators in python
# = , += , -= , *= , /= , //= , %= , **=
# x = 10
# print(x)
# x += 5  # x = x + 5
# print(x)
# x -= 3  # x = x - 3
# print(x)
# x *= 2  # x = x * 2
# print(x)
# x /= 4  # x = x / 4
# print(x)
# x //= 3  # x = x // 3
# print(x)
# x %= 2  # x = x % 2
# print(x)
# x **= 4  # x = x ** 4
# print(x)
# # //=
# x//=2
# print(x)
# # end lesson 26
# # start lesson 27
# # comparison operators in python
# # == , != , > , < , >= , <=
# x = 10
# y = 5
# print(x == y)  # False
# print(x != y)  # True
# print(x > y)  # True
# print(x < y)  # False
# print(x >= y)  # True
# print(x <= y)  # False
# end lesson 27
# start lesson 28
# Type conversion in python
# str() # to convert a value to string
# x = 10
# print(x)
# print(type(x))
# x = str(x)
# print(x)
# print(type(x))
# tuple() # to convert a value to tuple
# x="Hello"
# y=[1,2,3,4]
# e={"A","B","C"}
# f=("name","Alice","age",25)
# e={"A","B","C"}
# f={"name":"Alice","age":25}
# print(tuple(x))
# print(tuple(y))
# print(tuple(e))
# print(tuple(f))
# print(tuple(500))  # TypeError: 'int' object is not iterable
# list() # to convert a value to list
# y=(1,2,3,4)
# print(list(x))
# print(list(y))
# print(list(e))
# print(list(f))
# set() # to convert a value to set
# e=("A","B","C")
# # print(set(x))
# # print(set(y))
# # print(set(e))
# # print(set(f))
# # dict() # to convert a value to dictionary
# f="hello"
# e=((1,3),(2,4))
# x=[["name","Alice"],["age",25]]
# y={("name","Alice"),("age",25)}
# # print(dict(f))
# print(dict(e))
# print(dict(x))  
# print(dict(y))  
# end lesson 28
# start lesson 29
# User input in python
# fname = input("Enter your first name: ")
# lname = input("Enter your last name: ")
# print("Hello, " + fname + " " + lname + "!")
# age = input("Enter your age: ")
# print("You are " + age + " years old.")
# yearOfBirth = 2024 - int(age)
# print("You were born in " + str(yearOfBirth) + ".")
# end lesson 29
# start lesson 30
# slice email username and domain
# email ="abdelghanehaitham@gmail.com"
# print(email[0:17]) #abdelghanehaitham
# print(email[:email.index("@")])
# fName=input("Enter your first name : ").strip().title()
# emailDomain=input("Enter your email domain : ")
# userName=emailDomain[:emailDomain.index('@')]
# domain=emailDomain[emailDomain.index("@")+1:]
# print(f"Hello {fName}, your email is : {emailDomain} \nand user name {userName} and domain {domain}")
# end lesson 30
# start lesson 31
# partical your age full details
# age = input("Enter your age: ").strip()
# print(age)
# print(type(age))
# print(len(age))
# newAge=int(age)
# print('you lived for :')
# month = newAge * 12
# years= month // 12
# weeks= month * 4
# days = years * 24
# hours = days * 60
# minutes = hours * 60
# seconds = minutes * 60
# print(f" years : {years:,} \n months: {month:,} \n weeks: {weeks:,} \n days: {days:,} \n hours: {hours:,} \n minutes: {minutes:,} \n seconds: {seconds:,}")
# end lesson 31
# start lesson 32
# Control flow statements in python
# 1- if,elif,else statements
# userName="admin"
# cName="user"
# cPrice=150
# cDis=20
# if userName=="admin":
#     print("Welcome Admin")
# elif userName=="user":
#     print("Welcome User")
# else:
#     print("Welcome Guest")
#     if cPrice>100:
#         finalPrice=cPrice - cDis
#         print(f"Final price after discount is : {finalPrice}")
#     else:
#         print(f"Final price is : {cPrice}")
# # end lesson 32
# # start lesson 33
# # control flow statements part 2
# # nested if statement
# num = int(input("Enter a number: "))
# if num >=0:
#     if num == 0:
#         print("The number is zero.")
#     else:
#         print("The number is positive.")
# else:
#     print("The number is negative.")
# end lesson 33
# start lesson 10
# control flow statements part 3
# ternary operator
# please=" dasdas"
# age =input(f"Enter your age :{please}")
# ageNew="hello" if int(age) >= 18 else "hi"
# print(ageNew)
# end lesson 34
# start lesson 35
# calculate age advanced version and training  
# age =input("Enter your age : ").strip()
# unit = input("please choose the unit (years, months, weeks, days, hours, minutes, seconds): ").strip().lower()
# if unit == "months":
#     print(f"you lived for : {int(age) *12:,} months")
# elif unit == "weeks":
#     print(f"you lived for : {int(age) * 52:,} weeks")
# elif unit == "days":
#     print(f"you lived for : {int(age) * 365:,} days")
# end lesson 35
# start lesson 36
# membership operators in python
# in , not in
# string
# name ="haitham"
# print("h" in name)  # True
# print("z" in name)  # False
# print("H" not in name)  # True
# # list
# myList = [1, 2, 3, 4, 5]
# print(3 in myList)  # True
# print(6 in myList)  # False
# print(7 not in myList)  # True
# # using in and not in with if statement
# countryOne = ["USA", "Canada", "UK", "Australia"]
# discountOne= 20
# countryTwo = ["France", "Germany", "Italy"]
# discountTwo= 10
# myCountry = input("Enter your country: ").strip()
# # if myCountry in countryOne or countryTwo:
# #     if myCountry in countryOne:
# #         print(f"you are have discount:{discountOne}%")
# #     elif myCountry in countryTwo:
# #         print(f"you are have discount:{discountTwo}%")
# #     else:
# #         print("you are not have any discount")
# # else:
# #     print("you are not have any discount$$$$")
# if myCountry == 'USA' or myCountry == 'Canada' or myCountry == 'UK' or myCountry == 'Australia':
#     print(f"you are have discount:{discountOne}%")
# elif myCountry == 'France' or myCountry == 'Germany' or myCountry == 'Italy':
#     print(f"you are have discount:{discountTwo}%")
# else:
#     print("you are not have any discount$$$$")
# end lesson 36
# start lesson 37
# Loops in python
# while condition_is_true:
#     # code to be executed repeatedly
# count = 1
# while count<=5:
#     print(f"Count is: {count}")
#     count += 1
# print("Loop ended.")
# while loop with else
# count = 1
# while count <= 5:
#     print(f"Count is: {count}")
#     count += 1
# else:
#     print("Loop ended normally.")
# loop => while training 
# simple bookmark system
# websites = []
# allowedWebsites = 5
# while allowedWebsites >0:
#     website= input("Enter a website to bookmark: ").strip()
#     websites.append(website)
#     allowedWebsites -=1
#     print(f"You have {allowedWebsites} bookmarks left.")
# else:
#     print("You have reached the maximum number of bookmarks.")
#     print("Your bookmarked websites are:")
#     for site in websites:
#         print(f"- {site}")
# Loop break statement
# iterable object =>sequence [list,tuple,string,set,dictionary]
# count = 1
# while count <= 10:
#     if count == 6:
#         print("Breaking the loop at count 6.")
#         break
#     print(f"Count is: {count}")
#     count += 1
# print("Loop ended.")
# # loop =>for
# iterable = [1, 2, 3, 4, 5]
# for item in iterable:
#     print(f"Item is:{item}")
#     # odd or even 
#     if item % 2 ==0:
#         print(f"{item} is even")
#     else:
#         print(f"{item} is odd")
# loop => for training
# myRange = range(1,100)
# for number in myRange:
#     print(f"number is : {number}")
# # dictionary loop
# myDict={
#     "name":"Alice",
#     "age":25,
#     "is_student":True
# }
# for key in myDict:
#     print(f"key is : {key} and value is : {myDict[key]}")
#     print(f"key is : {key} and value is : {myDict.get(key)} %%%%")
# end lesson 37
# start lesson 38
# loop => for
# nested loop
# peoples = ["Alice", "Bob", "Charlie"]
# skills = ["Python", "Java", "C++"]
# for person in peoples:
#     print(f"Skills of {person}:")
#     for skill in skills:
#         print(f"- {skill}")
# peoples={
#     "Alice":{
#         "python":80,
#         "Django":70,
#         "Flask":60
#     },
#     "Bob":{
#         "Java":85,
#         "Spring":75,
#         "Hibernate":65
#     },
#     "Charlie":{
#         "C++":90,
#         "Qt":80,
#         "OpenGL":70
#     }
# }
# print(peoples["Alice"]["Django"])
# for person in peoples:
#     print(f"skills of {person}:")
#     for skill in peoples[person]:
#         print(f"-{skill}=> {peoples[person][skill]}%")
# break, continue , pass
# for number in range(1,11):
#     if number == 5:
#         print("Skipping number 5.")
#         continue
#     print(f"Number is: {number}")
# numbers=[1,2,3,4,5,6,7,8,9,10]
# # for number in numbers:
# #     if number == 5:
# #        break
# #     print(f"Number is: {number}")
# # pass
# for number in numbers:
#     if number == 5:
#         pass  # Placeholder for future code
#     print(f"Number is: {number}") # IndentationError: expected an indented block after 'if' statement on line 246
# loop advanced dictionary
# peoples={
#     "Alice":{
#         "python":80,
#         "Django":70,
#         "Flask":60
#     },
#     "Bob":{
#         "Java":85,
#         "Spring":75,
#         "Hibernate":65
#     },
#     "Charlie":{
#         "C++":90,
#         "Qt":80,
#         "OpenGL":70
#     }
# }
# print(peoples.items())
# for key,value in peoples.items():
#     print(f"this is the key :{key} and this is the value : {value}")
#     for skill,score  in value.items():
#         print(f"skill is : {skill} and score is : {score}")
# end lesson 38
# start lesson 39
# Function and return statement in python
# 1- function is a block of code which only runs when it is called
# 2- function is defined using the def keyword
# 3- function can accept parameters (arguments) and return data
# 4- function can have default parameter values
# 5- function can have variable-length arguments
# 6- function can be recursive (a function that calls itself)
# 7- function can be anonymous (lambda function)
# 8- function can be nested (a function inside another function)
# 9- function can have docstrings (documentation strings)
# 10- function can be imported from other modules
# 11- function can be assigned to variables
# 12- function can be passed as arguments to other functions
# 13- function can return multiple values
# 14- function can have type hints (annotations)
# define a function
# def greetUser(name: str) -> str:
#     """This function greets the user with their name."""
#     return f"Hello, {name}! Welcome to the Python course."
# # call the function
# userName = input("Enter your name: ").strip().title()
# greetingMessage = greetUser(userName)
# print(greetingMessage)
# end lesson 39
# start lesson 40
# function with default parameter value
# def calculateArea(length:float=2,width:float=1)->float:
#     """This function calculates the area of a rectangle."""
#     return length * width
# def calculateArea(length:float,width:float)->float:
#     """This function calculates the area of a rectangle."""
#     return length * width
# print(calculateArea(2,4))  # using default values
# def sayHello()->None:
#     """This function prints a hello message."""
#     print("Hello! This is a simple function without parameters and return value.")
# sayHello()
# end lesson 40
# start lesson 41
# function pack and unpacking arguments
# def displayInfo(*args, **kwargs) -> None:
#     """This function displays positional and keyword arguments."""
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)
# # call the function with positional arguments
# displayInfo("Alice", 25, True)
# # call the function with keyword arguments
# displayInfo(name="Bob", age=30, is_student=False)
# # call the function with both positional and keyword arguments
# displayInfo("Charlie", 22, is_student=True, city="New York")
# # unpacking arguments from a list and dictionary
# positionalArgs = ["David", 28, False]
# keywordArgs = {"name": "Eve", "age": 26, "is_student": True}
# displayInfo(*positionalArgs)
# displayInfo(**keywordArgs)
# function default parameter value with packing and unpacking
# def createProfile(name: str, age: int = 18, **additionalInfo) -> dict:
#     """This function creates a user profile dictionary."""
#     profile = {
#         "name": name,
#         "age": age
#     }
#     profile.update(additionalInfo)
#     return profile
# print(createProfile("Alice", location="USA", occupation="Engineer"))
# print(createProfile("Bob", 25, hobbies=["Reading", "Traveling"]))
# print(createProfile("Charlie", 30, is_student=True))
# end lesson 41
# start lesson 42
# Function Packing Unpacking Keyword Arguments
# def show_skills(*skills:str)->None:
#     print(type(skills))
#     for skill in skills:
#         print(f"- {skill}")
# show_skills("Python", "Java", "C++", "JavaScript")
# def show_user_info(**user_info:dict)->None:
#     print(type(user_info))
#     for key, value in user_info.items():
#         print(f"{key}: {value}")
# show_user_info(name="Alice", age=25, city="New York", is_student=True)
# end lesson 42
# start lesson 43
# function scope in python
# global variable
# x = 10  # global variable
# def myFunction() -> None:
#     # local variable
#     y = 5  # local variable
#     print(f"Inside the function, x = {x}")  # accessing global variable
#     print(f"Inside the function, y = {y}")  # accessing local variable
# myFunction()
# print(f"Outside the function, x = {x}")  # accessing global variable   
# # print(f"Outside the function, y = {y}")  # NameError: name 'y' is not defined
# # modifying global variable inside a function
# def modifyGlobal() -> None:
#     global x  # declare x as global
#     x += 5  # modify global variable
#     print(f"Inside the function after modification, x = {x}")
# modifyGlobal()
# print(f"Outside the function after modification, x = {x}")
# end lesson 43
# start lesson 44
# function recursion in python
# def factorial(n: int) -> int:
#     """This function returns the factorial of a number using recursion."""
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# number = int(input("Enter a number to calculate its factorial: "))
# result = factorial(number)
# print(f"The factorial of {number} is {result}.")
# question: What will happen if we pass a negative number to the factorial function?
# answer: The function will enter an infinite recursion because there is no base case for negative numbers, leading to a RecursionError.
# question: we want to write function that take this param "wwwoooooorrldd" and return "world"
# def remove_duplicates(word:str)->str:
#     if len(word) == 1:
#         return word #base case
#     if word[0] == word[1]:
#         return remove_duplicates(word[1:])
#     if word[0] != word[1]:
#         return word[0] + remove_duplicates(word[1:])
# print(remove_duplicates("wwwoooooorrldd"))
# end lesson 44
# start lesson 45
# lambda function in python
# 1- lambda function is a small anonymous function
# 2- lambda function can take any number of arguments but can only have one expression
# 3- lambda function is defined using the lambda keyword
# 4- lambda function can be used wherever function objects are required
# 5- lambda function can be assigned to variables
# 6- lambda function can be used with built-in functions like map(), filter(), and reduce()
# 7- lambda function can be used with higher-order functions
# 8- lambda function can be used in list comprehensions
# # syntax
# lambda arguments: expression
# # example 1
# add = lambda x, y: x + y
# def say_hello(name,age): return f"hello {name} your age is {age}"
# hello = lambda name,age: f"hello {name} your age is {age}"
# print(say_hello.__name__)
# print(hello.__name__)
# end lesson 45
# start lesson 46
# Files Handling Part One Intro
# "a" => append mode open file for writing, appending to the end of the file if it exists
# "r" => read mode open file for reading (default mode)
# "w" => write mode open file for writing, truncating the file first if it exists
# "x" => exclusive creation mode open file for exclusive creation, failing if the file already exists
# import os
# print(os.getcwd()) # get current working directory main
# print(os.path.dirname(os.path.abspath(__file__))) # directory of the current file
# # change current working directory
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# print(os.getcwd()) # get current working directory after change
# print(os.path.abspath(__file__)) # get full path of the current file
# file = open("haitham.txt") #read by default
# file = open (r"c:\\Users\\abdel\\OneDrive\\Desktop\\Learn-python\\haitham.txt")  # absolute path
# # end lesson 46
# # start lesson 47
# #  Files Handling Part 2 Read Files
# myFile = open("haitham.txt", "r")  # read mode
# print(myFile)  # <_io.TextIOWrapper name='haitham.txt' mode='r' encoding='cp1252'>
# print(type(myFile))  # <class '_io.TextIOWrapper'>
# print(myFile.name)  # haitham.txt
# print(myFile.mode)  # r
# print(myFile.read())
# print(myFile.read(23))
# print(myFile.readline(2))
# for line in myFile:
#     print(line)
#     if line.startswith('7'):
#         break
# myFile.close()
# end lesson 47
# start lesson 48
# Files Handling Part 3 Write and Append In Files
# myFile = open("haitham.txt", "w")  # write mode
# myFile.write("\nThis line is added in write mode.\n" * 5)
# myFile.close()
# myList = ["line 1\n", "Line 2\n", "Line 3\n"]
# myFile = open("haitham.txt", "w")  # write mode
# myFile.writelines(myList)
# append mode
# myFile = open("haitham.txt", "a")  # append mode
# myFile.write("\nThis line is added in append mode.\n" * 5)
# myFile.close()
# truncate() # to truncate the file to a specified size
myFile = open("haitham.txt", "a")  # append mode
myFile.truncate(5)  # truncate the file to 5 bytes