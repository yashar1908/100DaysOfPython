name = "Yash"
gender = 'm'
age = 19
percentile = 91.157
hindu = True

#type() function returns the datatype of the arguement
#syntax: type(arguement)

# print(type(name))
# print(type(age))
# print(type(percentile))
# print(type(hindu))
# print(type(gender)) #this also gives output as string.

#Type Conversion or Type Casting:
a = 123
print(type(a))

#I. Integer to String
stra = str(a)
print(type(stra)) #note that a is still an integer, stra is its string counterpart

#II. Integer to float 
flta = float(a)
print(type(flta))

#III. Float to string 
fstr = str(flta)
print(type(fstr))

#IV. String to float 
s = "143.25"
fs = float(s)
print(type(fs))

#V. String to Integer 
si = "1445"
ints = int(si)
print(type(ints))


#All above were implicit conversions.
#Trying explixits:

#I. Float to Int
fl = 143.75
eif = int(fl) #slices the decimal part (doesnt round off, just removes the decimal)
print(eif, type(eif))

## Does bool get converted to string?
strhindu = str(hindu)
print(strhindu) #Yes it does

## bool gets converted to integer?
inthindu = int(hindu)
print(inthindu) #Yes, it doea, True becomes 1 and False becomes 0.



