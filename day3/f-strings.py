# strings formating in python
# STrings formatting can be done in python using the formate method 
price = 49
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

val = "Geeks"
print(f"{val} for {val} is a portal for {val}.")
name = "Tushar"
age = 23 
print(f"Hello, my nmae is {name} and I'm {age} years old" )

print(f"{2 * 30}")

letter  = "Hey my name is {} and I am from {0}"
country = "India"
name = "Harry"

print(letter.format(country,name))
print(f"Hey my name is {name} and  I am from {country}")
print(f"We use f-string like this: Hey nmae is {{name}} and I ma from {{country}}")
pric = 49.999

txt = f"For only {price:.2f} dollars!"
print(txt)
print(txt.format())
print(type(f"{2*30}"))


