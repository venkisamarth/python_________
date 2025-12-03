# class Animal: 
#     def __init__(self,name,species): 
#         self.name = name 
#         self.species = species

#     def make_sound(self): 
#         print("sound made by the animal")

# class Dog(Animal): 
#     def __init__(self,name,breed): 
#         Animal.init__(self,name,species= "Dog")
#         self.breed = breed
#     def make_sound(self): 
#         print("Bark")



# class Animal: 
#     def __init__(self,name,species): 
#         self.name = name 
#         self.species = species

#     def make_sound(self): 
#         print("sound made byt he animal")
# class Dog(Animal): 

#     def __init__(self, name, breed): 
#         Animal.__init__(self,name,species="Dog")
#         self.breed = breed

#     def make_sound(self):
#         print("Bark")
# dog=  Dog("Dog", "Doggerman")
# d.make_sound()

# a.Animal("Dog","Dog")
# a.make_sound()

class Animal: 
    def sound(self): 
        return "Some sound"
class Dog(Animal): 
    def sound(self): 
        return "Bark"
    
obj = Dog()
print(obj.sound())
obj1 = Animal()
print(obj1.sound())

class Vehicle: 
    def start(self):
        return "Vehicle started"
class Car(Vehicle): 
    def drive(self): 
        return "Car is driving"
my_car= Car()
print(my_car.drive())
print(my_car.drive())
print(my_car.start())

class Person:
    def __init__(self,name):
        self.name = name 

class Student(Person):
    def __init__(self,name,grade): 
        super().__init__(name)
        self.grade = grade

stu = Student("Venki", "A")
print(stu.name) 
print(stu.grade)     

class Parent: 
    def __init__(self): 
        print("Parent constructor called")

class child(Parent): 
    def __init__(self): 
        super().__init__()
        print("child constructor")
obj = child()
print(obj)


class Animal: 
    def sound(self): 
        return "some sound"
    
class Dog(Animal): 
    def sound(self): 
        Parent_sound= super().sound()
        return Parent_sound + "+ Bark"
obj = Animal()
print(obj.sound())
obj1 = Dog()
print(obj1.sound())


class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)   # initializes name from parent
        self.roll = roll

s = Student("Venki", 25)
print(s.name)
print(s.roll)
    

class Person: 
    def __init__(self,name):
        self.name = name 
class Student(Person):
    def __init__(self,name, roll): 
        super().__init__(name)
        self.roll= roll

s= Student("Venki",23) 
print(s.name)
print(s.roll)















        




