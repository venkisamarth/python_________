numbers = [1,2,3,4,5]
double  = map(lambda x: x*2, numbers)
print(list(double))

# filter built in funciton in python
numbers = [1,2,3,3,4,5]
evens = filter (lambda x : x %2 ==0, numbers)
print(list (evens))

# reduce built in function i python
from functools import reduce
numbers = [ 1,2,3,4,4]
red_= reduce(lambda x,y: x+y,numbers)

print(sum)

def cube(x):
    return x *x*x

print(cube(3))

l = [ 1, 2, 3, 4, 5,6]
newl = []
for item in l: 
    newl. append(cube(item))
newl  = list(map(lambda x : x*x*x, numbers))
print(list(newl))

# filter function in python 
def filter_function(a):
    return a>2

newnewl = list(filter(filter_function,l))
print(newnewl)


# calculate the sum of the numbers using the reduce funciton 4
def mysum(x,y):
    return x + y
sum = reduce (lambda x , y :x+y, numbers)
print(sum)

sum = reduce(mysum,numbers)
print(sum)






