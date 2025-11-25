# enumerate function in python
# The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time.
#  Here's a basic example of how it works:

fruits = ["apple", "banana", "mango"]
for index, fruit in  enumerate(fruits):
    print(index, fruit)

list = [ "venkatesh ", 19 , "jayappa", "sachin"]
for index, list in enumerate(list, start=1):
    print(index, list)

for index, fruit in enumerate(fruits):
    print(f"{index+1}: {fruit}")

colors = ("red", "white", "orange", "safren")
for  index , color in enumerate(colors): 
    print(f"{index+1}:  {color}")

a = "venkatesh " 
for index, c in enumerate(a): 
    print(f"{index+1}: {c}")
marks = [89, 90, 70, 89, 90]
for index , value in enumerate(marks, start=1): 
    print(index, value)
    if index ==3: 
        print("this is the max marks")



