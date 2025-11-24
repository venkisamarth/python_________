# Exception Handling
# Exception handling is the process of responding to unwanted or unexpected events when a computer program runs.
# Exception handling deals with these events to avoid the program or system crashing, and without this process, 
# exceptions would disrupt the normal operation of a program.


# Exception in python 
# python try.. except

# try:
#     num = int(input("Enter an iinteger: "))
# except ValueError:
#     print("Number enterd is not an interger ")

# a = input("Enter the number: ")
# print(f"Muliplication  table {a} is : ")
# try: 
#     for i in range(1, 11):
#         print(f"{int(a)} x {i} = {int(a)*i}")
# except: 
#     print("Invalid input!")

# print("some imp lines of code")

# print("End of progam")

try: 
    num = int(input("Enter the integer: "))
    a = [6, 7]
    print(a[num])

except ValueError: 
    print("Number is not an integer")
except IndexError:
    print("Indix Error")

