# the dir() method
x = [ 1,2,3,4,5]
print(dir(x))
# dir(): The dir() function returns a list of all the attributes and methods 
# t is a useful tool for discovering what you can do with an object.
class Person: 
    def __init__(self,name, age): 
        self.name = name
        self .age = age

p = Person("john", 30 )
print(p.__dict__)
print(p.__doc__)


# The hep() method in python 
print(help(str))

# Help on class str in  module __builtins__

# class str(object)
#  |  str(object='') -> str
#  |  str(bytes_or_buffer[, encoding[, errors]]) -> str
#  |
#  |  Create a new string object from the given object. If encoding or
#  |  errors is specified, then the object must expose a data buffer
#  |  that will be decoded using the given encoding and error handler.
#  |  Otherwise, returns the result of object.__str__() (if defined)
#  |  or repr(object).
#  |  encoding defaults to sys.getdefaultencoding().
#  |  errors defaults to 'strict'.

class Person: 
    def __init__(self,name,age):
        self.name = name
        self.age= age
        self.version = 1 

p = Person("johan", 30)
print(p.__dict__)

print(help(Person))
        

