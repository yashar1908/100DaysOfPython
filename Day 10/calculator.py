def add(x,y):
    return x+y;
def subtract(x,y):
    return x-y;
def multiply(x,y):
    return x*y;
def divide(x,y):
    return x/y;

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
};


print("Welcome to the calculator program!");
num1 = float(input("Enter the first number: "));
print("+\n-\n*\n/");
op = input("Pick an operation: ");
num2 = float(input("Enter the second number: "));
result = operation[op](num1, num2);
print(num1,op,num2,"=",result);