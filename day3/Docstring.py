# Docstring in python

# python docstrings are the strings literls that appears  right after 
# the defination of function method, class or module 
def square(n):
    """Takes  in a number n returns the square of n"""
    print(n**2)
square(5)

# Here is another example
def add(num1, num2):
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num1 + num2

# python comments vs Docstrings

# python comments

# Comments are descriptions that help
# programmers better understand the intent 
# and functionality of the program. They are 
# completely ignored 
# by the Python interpreter.

# python docstrings
# As mentioned above, Python docstrings are strings used right after the definition of a function, method, class, or module (like in Example 1). They are used to document our code.

# We can access these docstrings using the doc attribute.

def square(n):
    """ Takes in a number  n, returns """
    return n**2

print(square.__doc__)







