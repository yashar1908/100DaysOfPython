#we can also create a list of lists in python.
fruits = ["apple","banana","mango","pineapple"]
vegetables = ["carrot", "radish","beetroot"]
grocery = [fruits,vegetables]
print(grocery[0:])
#referencing elements in a nested list
'''consider a nested list like a 2 dimensional array 
any element in a nested list is referenced as such:
listName[i][j]
the first index is the index of the list inside the nested list in which
our desired element is
and the next element is the index of the element in the list 
so if you want to refer to appele in grocery list,
"apple" = grocery[0][0] //True
"radish" = grocery[1][1]
"beetroot" = grocery[1][2]
and so on'''
