# # python sets 
# # Sets are unordered collection of data items. 
# # They store multiple items in a single variable.
# # Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate 
# # items.

# info = {"Caral", 19 , False, 5,9,19}
# print(info)

# # accessing set items 
# for item in info:
#     print(item)

# # i = 0 
# # while i < len(info):
# #     print(info[i])
# #     i = i+1

# # my_set = {"apple", "banana", "cherry"}
# # items  = list(my_set)
# # i = 0 
# # while  i <len(items ):
# #     print(item[i])
# #     i = i +1 

# # my_set = {10, 20 , 30, 40}
# # it = iter(my_set)
# # while True: 
# #     try:
# #         print(next(it))
# #     except StopIteration:
# #         break

# i = 1 
# while i <=5:
#     print(i)
#     i = i +1


# n = 5 
# while n> 0 :
#     print(n)
#     n  = n- 1


# # example 
# i = 2 
# while i <= 10:
#     print(i)
#     i = i + 2 


# n= 10 
# i = 1 
# total  = 0 
# while i <=n: 
#     total =total + 1
#     i = i +1 
# print("sum:", total)

# text = "python"
# i = len(text)- 1 
# reverse = ""
# while i >=0:
#     reverse +=text[i]
#     i -=1 

# print(reverse)


# s= { 2,4, 3, 6}
# print(s)
# info= {"caral",19, False, 5, 9}
# print(info)

# harry = set()
# print(type(harry))

# for value  in info:
#     print(value)

# joing sets  
# sets in python more or less work in the same way as sets in mathematics we can perform 

# i union and update
cities = {"Tokyo", "Marid", "Berlin", "Delhi"}
cities2 = { "Tokyo" , "Seoul", "Kabul", "madrid"}
cities3 = cities.union(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.update(cities2)
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
print(cities.difference(cities2))

# set method in python
cities = {"tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Sroul", "Marid"}
print(cities.isdisjoin(cities2))












