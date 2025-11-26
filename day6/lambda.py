def double(x):
    return x * 2
a=lambda x: x*2
print(a(3))

def multiply(x,y):
    return x * y

a=lambda  x,y:print(f'{x} *{y}={x*y}')
print(a(3,4))

def double(x):
    return x *2 
def appl(fx, value):
    return 6 + fx(value)
double  = lambda x : x* 2
cube = lambda x : x *x *x

avg =  lambda x , y , z: (x+y +z)/3

print(double(5))
print(cube(4))
print(avg(3,4,10))
print(appl(lambda x: x * x , 2))
