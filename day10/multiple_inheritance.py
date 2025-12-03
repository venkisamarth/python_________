class HR: 
    def hr_details(slef): 
        return "HR: Leave balcne = 12 days"
class Payroll:
    def salary_details(self): 
        return "Payroll: Slary = 50,000 INR"
class Employee(HR,Payroll): 
    def employee_info(slef): 
        return "Employee:Venki"
emp = Employee()
print(emp.employee_info())
print(emp.hr_details())
print(emp.salary_details())


class Engine: 
    def engin_type(self): 
        return "Engine: v8 Petrol Engine"
class Body: 
    def body_type(self): 
        return "Body: suV Body Design"
class Car(Engine, Body):
    def car_info(self):
        return "Car: Range Rover"

c = Car()
print(c.car_info())
print(c.engine_type())
print(c.body_type())

class Sports:
    def sport(self):
        return "Sports: Football Player"

class StudentProfile(Academics, Sports):
    def profile(self):
        return "Student: Nishu"

sp = StudentProfile()
print(sp.profile())
print(sp.marks())
print(sp.sport())