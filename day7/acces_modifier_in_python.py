class Employee: 
    def __init__(self):
        self.__name = "Harry"
a = Employee()
# print(a.__name) cannot beaccesse ddirecty 
print(a._Employee__name)# cannot be accesse directly


# name mangling in python
print(a.__dir__())

class student: 
    def __init__(self, name, age):

        self.name= name
        self.age= age

obj1 = student("venki", 12)
print(obj1.name)







