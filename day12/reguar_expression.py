import re
txt= "I have 2 cars and 3 bikes"
result = re.findall(r'\d+',txt)
print(result)

import re 
txt = "Ptyhon123Programming"
result = re.findall(r'[a-zA-Z]+',txt)
print(result)

import re

email = "venkat@gmail.com"

pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
print(re.match(pattern, email))


text = "Hello world"

result = re.match(r"Hello", text)
print(result)



import re

text = "Python is awesome"

result = re.sub(r"\s+", "-", text)
print(result)
