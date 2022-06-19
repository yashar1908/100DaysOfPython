#To be more specific with assigning arguments to parameters, keyword arguments approach is used 
def details(name, id):
    print("Confirming the student details:");
    print("Name of the student:",name);
    print("Id of the student:",id);

details(name = "Yash", id = 1);
details(id = 2, name = "Angela");

'''
Now you can switch the position of the arguments because youre specifying which argument is being assigned to which parameter.
'''