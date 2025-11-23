# recursion in python 

# recursion is the process of deining something in terms of itself

# def factorial(n):
#     if(n ==1 or n ==0):
#         return 1 
#     else: 
#         return (  n *factorial(n-1))
    
# print(factorial(6))
# print(factorial(7))

def factorial(n):
    if (n==0 or n==1):
        return 1
        
    else:
        return n*factorial(n-1)
        

print(factorial(9))




