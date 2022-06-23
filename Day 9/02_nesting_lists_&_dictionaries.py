#Example of nested list:
list1 = [[1,2,3], [4,5,6], [7,8,9]];
print(list1) #prints the list 
print(list1[2][1]); #syntax: list1[index of list2][index of element in list2] where list2 is a sub-list in list1
#So the above print statement prints second element of third list in list1.

#Nesting lists in a dictionary:
dict1 = {1:[1,2,3], 2:[4,5,6], 3:[7,8,9],};
print(dict1[1]); 
#Syntax: dict = {key1:list1, key2:list2, key3:list3, .... keyN:listN};

#Nesting dictionaries in a dictionary
dict2 = {
    'a':{1:"Yash", 2:"Shreya",}, 
    'b':{3:"Angela", 4:"John"},
    };
print(dict2['a']); #Prints the value corrresponding to key 'a' which is the first nested dictionary
print(dict2['b'][3]); #Prints the value corresponding to key 3 in the dictionary corresponding to key 'b'


#Example of nesting list in a dictionary
#If you want to store all the cities you travelled in a specific country then you can nest lists in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"], 
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
    };

#Ecample of nesting a dictionary in a dictionary
#In addition to the tracel_log, you also want to keep track of how many times you visited each city.
travel_log_frequency = {
    "France": {
        "Paris" : 4,
        "Lille" : 1,
        "Dijon" : 6,
    },
    "Germany": {
        "Berlin" : 8,
        "Hamburg" : 2,
        "Stuttgart" : 3,
    },
};

print(travel_log_frequency["France"]["Paris"]);

#Nesting a dictionary in a list 
super_list = [
    {
        1:10,
        2:11,
    },
    {
        3:12,
        4:13,
    },
];
print(super_list[0]);
print(super_list[1][4]);