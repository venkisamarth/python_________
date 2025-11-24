# python Dictionaries
# Dictionaries are ordered collection of
# data items. They store multiple items
# in a single variable. Dictionary items
# are key-value pairs that are separated 
# by commas and enclosed
# within curly brackets {}.

info = {"name": "keran", "age":19, "eligable":True}
print(info)

# Accessing Dictionary items
info = {'name':"leran", "age": 19, "eligable": True}
print(info["name"])
print(info.get('eligable'))

# accessing multiple values
info = {"name":"karna", "age": 19, "eligable":True} 
print(info.values())
print(info.keys())
print(info.items())

# accessing key-value pairs

info = {"name":"karna", "age": 19, "Eligable":True}
print(info.items())

info = {"name":"karn", "age":19, "eligable":True}
print(info)

print(info.items())
for key,value in info.items():
    print(f"The value corresponding to the key {key} is {value}")

# Dictonary Methods

# Dictionary uses several built-in methods
# for manipulation.
# They are listed below

# update():
# The update() method updates the value of the key provided to it if item already exists

info = {"nam":"karna", "age":19, 'eligable':True}
print(info)
info.update({"age":20})
info.update({"Dob":2001})
print(info)

# Removing  items from Dictionary

info = {"name": "karna", "age":19, "eleigable":True}
info.clear()
print(info)

info = {"name": "karan", "age":19, "eligable":True}
info.pop("eligable")
print(info)

info.popitem()
print(info)
# del info["age"]

print(info)

info = {"name":"karna", "age":19, "DOB":"2003"}
print(info)


del info
print(info)

ep1 = {122:45, 123:89,567:69}
ep2= {222:67, 556:90}
ep1.update(ep2)
ep1.clear()

ep1.popitem()
del ep1[122]

print(ep1)
























































