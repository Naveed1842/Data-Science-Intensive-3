#https://www.stavros.io/tutorials/python/
                                                    # Properties
#Python is strongly typed (i.e. types are enforced), dynamically, implicitly typed (i.e. you don't have to declare variables),
#case sensitive (i.e. var and VAR are two different variables) and object-oriented (i.e. everything is an object).
                                                        # Getting help
help(5)
# Help on int object:
# (etc etc)

dir(5)
# ['__abs__', '__add__', ...]

abs.__doc__
# 'abs(number) -> number

# Return the absolute value of the argument.'

                                                        # Syntax
myvar = 3
myvar += 2
myvar
#5
myvar -= 1
myvar
#4
"""This is a multiline comment.
The following lines concatenate the two strings."""
mystring = "Hello"
mystring += " world."
print mystring
# Hello world.

# This swaps the variables in one line(!).
# It doesn't violate strong typing because values aren't
# actually being assigned, but new objects are bound to
# the old names.
myvar, mystring = mystring, myvar

                                                        # Data Types
sample = [1, ["another", "list"], ("a", "tuple")]
mylist = ["List item 1", 2, 3.14]
mylist[0] = "List item 1 again" # We're changing the item.
mylist[-1] = 3.21 # Here, we refer to the last item.
mydict = {"Key 1": "Value 1", 2: 3, "pi": 3.14}
mydict["pi"] = 3.15 # This is how you change dictionary values.
mytuple = (1, 2, 3)
myfunction = len
print myfunction(mylist)

mylist = ["List item 1", 2, 3.14]
print mylist[:]
# ['List item 1', 2, 3.1400000000000001]
print mylist[0:2]
# ['List item 1', 2]
print mylist[-3:-1]
# ['List item 1', 2]
print mylist[1:]
# [2, 3.14]
# Adding a third parameter, "step" will have Python step in
# N item increments, rather than 1.
# E.g., this will return the first item, then go to the third and
# return that (so, items 0 and 2 in 0-indexing).
print mylist[::2]
# ['List item 1', 3.14]
mylist[1::]
# Out[32]: [2, 3.21, 3]
mylist[1::2]
# Out[33]: [2, 3]

                                                    # Strings
print "Name: %s    ...: Number: %s    ...: String: %s" % ("Poromenos", 3, 3*"-")
# Name: PoromenosNumber: 3String: ---

# WARNING: Watch out for the trailing s in "%(key)s"
print "This %(verb)s a %(noun)s." % {"noun": "test", "verb":"is"}
# This is a test.

                                                    # Flow control statements
rangelist = range(10)
for number in rangelist:
    # Check if number is one of 
    # the numbers in the tuple.
    if number in (3, 4, 7, 9):
        # "Break" terminates a for without
        # executing the "else" clause.
        break
    else:
        # "Continue" starts the next iteration
        # of the loop. It's rather useless here.
        # as it's the last statement of the loop.
        continue
else:
    # The "else" clause is optional and is
    # executed only if the loop didn't "break"
    pass # Do nothing
    
if rangelist[1] == 2:
    print "The second item (lists are 0-based) is 2"
elif rangelist[1] == 3:
    print "The second item (lists are 0-based) is 3"
else:
    print "Dunno"

while rangelist[1] == 1:
    pass
    
                                                        # Functions
# Same as def funcvar(x): return x + 1
funcvar = lambda x: x + 1
print funcvar(1)
# 2

# an_int and a_string are optional, they have default values
# if one is not passed (2 and "A default string", respectively).
def passing_example(a_list, an_int=2, a_string="A default string"):
    a_list.append("A new item")
    an_int = 4
    return a_list, an_int, a_string

my_list = [1, 2, 3]
my_int = 10
print passing_example(my_list, my_int)
#([1, 2, 3, 'A new item'], 4, "A default string")
my_list
#[1, 2, 3, 'A new item']
my_int
#10
 
                                                                    # Class
class MyClass(object):
    common = 10
    def __init__(self):
        self.myvariable = 3
    def myfunction(self, arg1, arg2):
        return self.myvariable

    # This is the class instantiation
classinstance = MyClass()
classinstance.myfunction(1, 2)
# 3
# This variable is shared by all classes.
classinstance2 = MyClass()
classinstance.common
# 10
classinstance2.common
# 10
# Note how we use the class name
# instead of the instance.
MyClass.common = 30
classinstance.common
# 30
classinstance2.common
# 30
# This will not update the variable on the class,
# instead it will bind a new object to the old
# variable name.
classinstance.common = 10
classinstance.common
# 10
classinstance2.common
# 30
MyClass.common = 50
# This has not changed, because "common" is
# now an instance variable.
classinstance.common
# 10
classinstance2.common
# 50

# This class inherits from MyClass. The example
# class above inherits from "object", which makes
# it what's called a "new-style class".
# Multiple inheritance is declared as:
# class OtherClass(MyClass1, MyClass2, MyClassN)
class OtherClass(MyClass):
    # The "self" argument is passed automatically
    # and refers to the class instance, so you can set
    # instance variables as above, but from inside the class.
    def __init__(self, arg1):
        self.myvariable = 3
        print arg1

classinstance = OtherClass("hello")
# hello
classinstance.myfunction(1, 2)
# 3
# This class doesn't have a .test member, but
# we can add one to the instance anyway. Note
# that this will only be a member of classinstance.
classinstance.test = 10
classinstance.test
# 10       


                                                                    # Exceptions
def some_function():
    try:
        # Division by zero raises an exception
        10 / 0
    except ZeroDivisionError:
        print "Oops, invalid."
    else:
        # Exception didn't occur, we're good.
        pass
    finally:
        # This is executed after the code block is run
        # and all exceptions have been handled, even
        # if a new exception is raised while handling.
        print "We're done with that."

some_function()
#Oops, invalid.
#We're done with that.

                                                                  # Importing
import random
from time import clock

randomint = random.randint(1, 100)
print randomint
#60

                                                                    #File I/O
import pickle
mylist = ["This", "is", 4, 13327]
# Open the file C:\\binary.dat for writing. The letter r before the
# filename string is used to prevent backslash escaping.
myfile = open(r"C:\\binary.dat", "w")
pickle.dump(mylist, myfile)
myfile.close()

myfile = open(r"C:\\text.txt", "w")
myfile.write("This is a sample string")
myfile.close()

myfile = open(r"C:\\text.txt")
print myfile.read()
# 'This is a sample string'
myfile.close()

# Open the file for reading.
myfile = open(r"C:\\binary.dat")
loadedlist = pickle.load(myfile)
myfile.close()
print loadedlist
# ['This', 'is', 4, 13327]

                                                                   # Miscellaneous
lst1 = [1, 2, 3]
lst2 = [3, 4, 5]
print [x * y for x in lst1 for y in lst2]
# [3, 4, 5, 6, 8, 10, 9, 12, 15]
print [x for x in lst1 if 4 > x > 1]
# [2, 3]
# Check if a condition is true for any items.
# "any" returns true if any item in the list is true.
any([i % 3 for i in [3, 3, 4, 4, 3]])
# True
# This is because 4 % 3 = 1, and 1 is true, so any()
# returns True.

# Check for how many items a condition is true.
sum(1 for i in [3, 3, 4, 4, 3] if i == 4)
# 2
del lst1[0]
print lst1
# [2, 3]
del lst1

number = 5

def myfunc():
    # This will print 5.
    print number

def anotherfunc():
    # This raises an exception because the variable has not
    # been bound before printing. Python knows that it an
    # object will be bound to it later and creates a new, local
    # object instead of accessing the global one.
    print number
    number = 3

def yetanotherfunc():
    global number
    # This will correctly change the global.
    number = 3


