# # what are string in python 
# in python, anyting that you close betweeen single or doule quotation marks is considerd 
# # a string. A String is essentially a seunce or arry of textual data. Strings are usd when working with unicode  characters
name = "venki"
print("Hello," + name)
print(type(name))

# multiline string

# If our string has multiple lines, we can create them like this:
a = """"
Lorem ipsum doler sit am
this is the muliline stings in python
"""
print(a)
# accessing the characters of a string
# In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.
print(name[0])
print([1])

for characets in name:
    print(characets)


name = "Harry"
friend = "Rohan"
anotherFriend = "Lovish"
apple = ''' He said  
Hi  harry 
"i want to eat an apple"'''

# print("Hello",+ name)
#print(apple)

print(name[0])
print(name[1])
print(name[2])
# print(name[5])

# print(name[5] # Throws and error)

print("lets use a for loop\n")
for character in apple:
    print(character)