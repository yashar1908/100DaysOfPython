#syntax = input(Prompt)

#simply taking input:
input("What is your name?\n");

#storing input in a variable
name = input("What is your name again?\n");
print("Oh! Hi,",name)

###VERY IMPORTANT###
#default datatype of any input is string and it needs to be converted before using
#eg if u input 123 as age then that age is stored as a string and you need to convert it to integer 
#demonstration:
age = input("What is your age? ")
print(type(age)) #says string

