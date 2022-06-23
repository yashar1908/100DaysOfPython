## Creating a Dictionary
#Syntax: dictionary_name = {key1:value1, key2:value2, .... , keyN:valueN};
student_marks = {"James":73, "Adrian":56, "Amanda":64};

#Developer way of formatting a dictionary creation code:
student_marks_withGoodFormat = {
    "James": 73, 
    "Adrian": 56,
    "Amanda": 64,
};

## Accessing data in a dictionary
print(student_marks["Adrian"]);
#The values of elements in dictionaries are accessed by the keys.
#So you provide the key of the element of the dictionary that you want to access.

#print(student_marks[73]); --> Gives an error because an element can't be accessed by its value but only by the key

## Adding new items to the dictionary (at the end of the dictionary)
student_marks["Yash"] = 100;
print(student_marks);

## Creating an empty dictionary
empty_dictionary = {};

## Wiping out all the entries of a dictionary: The approach is to set the dictionary equal to an empty dictionary.
student_marks = {};
print(student_marks); #prints an empty dictionary


###Task: Add all the items back into the dictionary student_marks.
student_marks["James"] = 73;
student_marks["Adrian"] = 56;
student_marks["Amanda"] = 64;
student_marks["Yash"] = 100;
print(student_marks);

## Edit an item in the dictionary
student_marks["James"] = 37; #just access an element using the key and then operate on its value
print(student_marks);

## Loop through a dictionary
for xyz in student_marks:
    print(xyz);
#The above line of code prints ONLY the keys of the dictionary but not the corresponding values.

#To print the values,
for key in student_marks:
    print(student_marks[key]);

#To print key with values,
for key in student_marks:
    print(key,":",student_marks[key]);