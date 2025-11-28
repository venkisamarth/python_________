# The super keword us used to refer to the parent class
class ParentClass: 
    def parent_method(slef): 
        print("This is  the parent method.")
class ChildClass(ParentClass): 
    # def parent_method(self):
    #     print("Harry")
    def child_method(slef): 
        print("This is the child method")

        super().parent_method()
child_object = ChildClass()
child_object.child_method()
child_object.parent_method()


class Employee: 
    def __init__(self, name,id): 
        self.name = name
        self.id = id
class Programmer(Employee): 
    def __init__(self,name,id,lang):
        self.name = name
        super().__init__(name,id)
        self.lang= lang
        # self.id = id
        # self.lang = lang



rohan = Employee("Rohan Das","420")
harry = Programmer("Harry","23434","python") 
print(rohan.name)
print(harry.name)

print(harry.name)
print(harry.id)
print(harry.name)

        






    