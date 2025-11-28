x = [1,2,3,3,4]
print(dir(x))

class Person: 
    def __init__(self,name,age):
        self.name= name
        self.age = age
p = Person('johan',30)
print(p.__dict__)

# The help() method

help(str)

# help on clss str in module __builtins__
# class on clss str in module builtins: 
# class str(object)
#     str(object = '')
#     str(b)


# >>> help(str)
# Help on class str in module builtins:

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

p = Person('john', 30)
print(p.__dir__)
print(help(Person))
print(p.__dict__)


tupe= (1,2,3,3,4)
print(dir())


print(help(str))