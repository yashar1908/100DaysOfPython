list1 = ["yash", "is", 19, "years", "old"]
#a list in python is like an array except it does not have any restriction
#on the type of data it stores (you can mix all data types together in one list)
listAll = ["string",19,80.45,True,'a']
#accessing an element of the list:

#print(list1[0])

#elements are indexed 0 through n-1 and can be accessed randomly by their indexes.

#using negative index to reference a value in the list:
#list[-1] will print the last element of the list
#list[-n] will print the first element of the list and so on.

#print("Last element of the list is:",list1[-1])

#changing the item in the list:
list1[1] = "arora"

#print(list1[1])

#adding item to end of the list: append(value)

#syntax: listName.append(value)
list1.append(True)
#print(list1[-1])

#inserting a value at random index of the list
#syntax: listName.insert(index,value)
list1.insert(2,"is")
print(list1[2])
