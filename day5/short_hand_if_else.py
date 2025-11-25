# If ... Else in One Line
a = 30 
b = 450 
print("a") if a>b else print("b")

a = 500 
b = 400
print("A") if a > b else print("=") if a == b else print("B")

print("a") if a>b else print("=") if a==b else print("B")

a = 100 
b = 200 
if a>b: 
    print("A")
else : 
    print("B")

a = int(input("Enter the value of a: "))
b = int (input("Enter the value of b: "))
if a>b:
    print("a is greater then b ")
elif a<b: 
    print("b is greater thean a")
else: 
    print("bothe a and b are equal")

c = 9 if a>b else 0
print(c)