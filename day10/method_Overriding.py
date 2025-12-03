# # <!-- Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method in a derived class. -->

# # <!-- The method in the derived class is said to override the method in the base class -->

# # When you create an instance of the derived class and call the overridden method, the version of the method in the derived class is executed, rather than the version in the base class.

# class shape: 
#     def ares(self):
#         pass

# class Circle(shape): 
#     def __init__(self,radius): 
#         self.radius = radius

#     def area(self): 
#         return 3.142 * self.radius * self.radius


# class Circle(Shape): 
#     def area(self): 
#         print("Calucating area....")
# class Cirlce(Shape): 
#     def __init__(self,radius): 
#         self.radius = radius
#     def area(self): 
#         print("Calulating area of a circle...")
#     super().area()
#     return 3.142 *self.radius * self.radius
class shape: 
    def __init__(self,x,y): 
        self.x = x 
        self.y = y
    def area(self): 
        return self.x* self.y
class Cirlce(shape): 
   def __init__(self,radius): 
       self.radius = radius
       super().__init__(radius,radius)

   def area(self):
       return 3.142 * super().area() 
   
c = Cirlce(5)
print(c.area)

       