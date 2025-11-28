# python class mthods 
class ExampleClass: 
    @classmethod
    def factory_method(cls,argumet1, argument2): 
        return cls(argumet1, argument2)
    
class Employee: 
    company = "Apple"
    def show(self): 
        print(f"The name is {self.name} and company is {self.company}")
        # cls.company = newCompay

e1 = Employee()
e1.name = "Harry"
e1.show()
e1.chnageCompany("Tesla")
e1.show()
print(Employee.company)