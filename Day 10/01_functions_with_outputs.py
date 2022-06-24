#Create a function called format_name which takes first and last name as input and outputs 
#the name in title case i.e. first letter caps of first name and last name 

#1. Using the title() function:
def format_name_1(fname, lname):
    fullname = fname + " " + lname;
    return fullname.title();

print(format_name_1("yAsh", "aRORA"));

#2. Without title():
def format_name2(fname, lname):
    fname_title = fname[0].upper();
    for char in fname[1:]:
        fname_title += char.lower();
    
    lname_title = lname[0].upper();
    for char in lname[1:]:
        lname_title += char.lower();
    
    fullname = fname_title + " " + lname_title;
    return fullname;

print(format_name2("yAsH", "aRORA"));