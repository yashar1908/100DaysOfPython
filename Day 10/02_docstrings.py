'''When you hover over the function signature of a built in python function you can see 
the documentation of the function showing what the function does'''
"a".upper() # -> example. "Return a copy of the string converted to uppercase" is the docstring

#Docstring of user-defined functions is made as so:
def add(x,y):
    """Used to return the sum of two numbers."""  #This is the docstring
    return x + y;

add(1,3) #Hover over the code and you can see the docstring

''' 
1. The docstring has to be enclosed in """ ..... """ three double quotes.
2. The dostring has to be written as the first line inside a function.
'''