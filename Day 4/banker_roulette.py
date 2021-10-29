# You are going to write a program which will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.
import random 
name_string = input("Enter names seperated by a comma")
names = name_string.split(", ")
l = len(names)
rand = random.randint(0,l-1)
print(names[rand],"will pay for the bill today!")
