# How importing works in python
# Importing in Python is the process of loading code from a Python module into the current script. This allows you to use the functions and variables defined in the module in your current script, as well as any additional modules that the imported module may depend on.

# To import a module in Python, you use the import statement followed by the name of the module. For example, to import the math module, which contains a variety of mathematical functions, you would use the following statement:
import math
import math 
result = math.sqrt(23)
print(result)

# from keyword in python
from math import sqrt as s
result = s(9)
print(result)

from math import sqrt, pi

result = sqrt(9)
print(result)  # Output: 3.0
print(pi) 

from math import pi ,sqrt 
print(pi)

from math import *
import math as m 

result = m.sqrt(34)
print(result)

import math 
print(dir(math))


