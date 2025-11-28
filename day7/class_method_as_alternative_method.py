# class Person: 
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age 
#     @classmethod
#     def from_string(cls,string): 
#         name, age = string.split(',')
#         return cls(name,int(age))
# Person = Person.from_string("John Doe, 30")
# print(Person)


# class Rectange: 
#     def __init__(self,width, height):
#         self.width = width
#         self.heigh = height

# class Rectangel: 
#     def __init__(self,width, height): 
#         self.width = width 
#         self.heigh = height 

#         @classmethod
#         def square(cls, size): 
#             return cls(size, size)
# rectangle = Rectangel.square(10)



class Employee: 
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary

    @classmethod
    def fromStr(cls,string): 
        return cls(string.split("-")[0],int(string.split('-')[1]))
    

e1 = Employee("Harry",12000)
print(e1.name)
print(e1.salary)


string = 'Johan-12000'

e2 =Employee.fromStr(string)
print(e2.name)
print(e2.salary)

class Person: 
    def __init__(self,name, age):
        self.name= name
        self.age= age
    @classmethod
    def form_string(cls,string): 
        name, age = string.split(",")
        return cls(name,int(age))
Person = Person.form_string("Johan Doe,30")
print(Person.name,Person.age)



        
