class StudentBasic:
    def basic(self):
        return "Name: Nishu"

class StudentAcademic(StudentBasic):
    def academic(self):
        return "Marks: 92%"

class StudentFullProfile(StudentAcademic):
    def full_profile(self):
        return "Sport: Football"

s = StudentFullProfile()
print(s.basic())
print(s.academic())
print(s.full_profile())


class  A: 
    def show(self): 
        return "class A mehtod "

class B(A): 
    def show(self): 
        return super().show()+" -> class Method"
class c(B): 
    def show(self): 
        return super().show()+" -> class C method"
obj = c()
print(obj.show())    