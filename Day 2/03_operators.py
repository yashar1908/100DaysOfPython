'''
Priority of operations:
()
**
* / left to right
+ - left to right

'''





#addition - + operator
sum = 7+3
sumfl = 7.1+3.8

#subtraction - '-' operator
diff = 7-3
difffl = 7.1-3.8

#multiplication - * operator
prod = 7*3
prodfl = 7.1*3.8

#division - / operator
div = 7/3
divw = 8/2 #note how it returns 4.0 and not 4.
divfl = 7.1/3.8

#exponent - ** operator
#a raised to n is written by a**n
eq = 64 == 2**6
# print(eq) #gives true
 

#remainder - % operator
rem = 8%5
# print(rem)

#does it work for float?
remfl = 7.1%3.8
# print(remfl)
#works perfectly fine

#note how I mentioned that division always returns a floating point value 
#iyw division to return an integer value then the following operator is used:

## // operator 
divFloor = 7//3
# print(divFloor) 
#outputs 2, and with 7/3 outputs 2.33 so // is just converting float to int by slicing decimals




 