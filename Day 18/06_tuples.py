# Syntax for declaring a tuple:
# tuple_name = (element1, element2, ... , elementN)

# Creating a tuple:
tup = (1,2,3,4)

# Accessing elements of tuple:
print(tup[0]) # prints 1

# Iterating through elements of a tuple
for element in tup:
    print(element, end = ' ')
print()
## Tuples are immutable. Once created, the elements of a tuple can't be changed, or deletedm or new elements added.
# tup[2] = 7  # Gives error because changing element of tuple is not allowed

# If you want to alter the elements of a tuple, you can assign the tuple to a list and do so.
list1 = list(tup)
list1.append(7)
print(list1)


# Unpacking a tuple
tup1 = ("Yash", "Arora", "yasharora1908@gmail.com")
fname, lname, email = tup1
print(fname)
print(lname)
print(email)
