#len() is a function to get length of a string
name = "Yash"
length = len(name)
random = len("Yash Arora")
print(random,"is greater than",length)
#syntax: len(arguement)

#len() is a string function and does not work for other datatypes.
#len(2345) gives an error but len("2345") outputs 4, and so on

#len() however works with char datatype and obviously always returns 1.
print(len('A'))
