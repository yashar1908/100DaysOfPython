#How to modify a global variable inside a function?
difficulty = 1;
def increase_difficulty():
    global difficulty; #signifying that the variable difficulty that we will reference in the function will be the global variable and not a local variable with the same name
    return difficulty + 1;

difficulty = increase_difficulty();
print(difficulty);
#Correct way of modifying a global variable is to create a function that returns its modified value 
#and then calling the function later rather than modifying global variable's value inside the function itself

#The concept of block scope does not exist in Python
def some_function():
    if 16 > 9:
        number = 16; #This variable has been created inside this if block
        #In Java/C++, a variable created inside an if block/for/while loop is local to those blocks of code 
        #But in python, a variable created inside such blocks is local to the enclosing function of that block.
        #ie if the variable was made in an if statement or loop inside a function then it will be local to that function 
        #and if the if statement/loop wasn't inside any function then the variables created in those blocks will be global variables.
    print(number);
    #Here the variable number is local to the enclosing function of the if statement, ie some_function()

#Also if there are multiple nested loops and if statements and then a variable inside this nesting, then too the variable will be local to the enclosing function.