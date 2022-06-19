#greet function without arguments:
def greet():
    print("Hi welcome to greet function.");
    print("This is a function with no arguments.");
    print("These statements are printed when the function is called");

#greet function with arguments:
def greet_with_name(name):
    print("Hello,",name);

greet_with_name("Yash");

'''
Difference between arguments and parameters:
parameter is the dummy variable name used in a function when you have to indicate that the function is going 
to take inputs.
argument is the actual input you give when you call the function
'''