def details(name, id):
    print("Confirming the student details:");
    print("Name of the student:",name);
    print("Id of the student:",id);

details("Yash", 1);
details(2, "Angela");

'''
When you give arguments ("Yash",1) the interpreter knows to associate 
the first argument with the first parameter and the second argument with the second parameter
hence name gets assigned yash and id gets assigned 1 

Same in the second case although your intention was to pass id,name but 
the first argument gets associated with the first parameter 
and the second argument gets associated with the second parameter.
So, naem gets assigned 2 and id gets assigned Angela 

This way of associating parameters with arguments based on their positions in the funnction signature
and their position when the funciton is called positional arguments approach.
This is the most widely used approach.
'''