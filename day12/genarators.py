def my_generator(): 
    yield 1 
    yield 2 
    yield 3 
gen = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))

# Example generatos to Print 1 - 5 
def numbers(): 
    for i in range(1,6):
        yield i 
import time
print(time.time())
for num in numbers(): 
    print(num) 
print(time.time())

def even_generator(n): 
    for i in range(0,n+1,2): 
        yield i 
for e in even_generator(10): 
    print(e)


# Example 
# generator EXpression(shouptcutl)

get = (x*x for x in range(5))
for g in get: 
    print(g)


def read_file(filename): 
    with open(filename,"r") as file: 
        for line in file: 
            yield line
for line in read_file("data.txt"): 
    print(line)
    