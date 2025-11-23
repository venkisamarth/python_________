# Create a python program capable of greeting 
# you with Good Morning, Good Afternoon and Good 
# Evening. Your program should use time module to
# get the current hour. Here is a sample program 
# and documentation
# link for you:

import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)
timestamp = time.strftime("%H")
print(timestamp)
timestamp = time.strftime("%M")
print(timestamp)
timestamp = time.strftime("%S")
print(timestamp)

import time
t = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))

if (hour>=0 and hour<12):
    print("Good Morning Sir!")
elif (hour>=12 and hour<17):
    print("Good AFternoon")
elif(hour>=17 and hour<0):
    print("Good night Sir!")








