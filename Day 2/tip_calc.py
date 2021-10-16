print("Welcome to the tip calculator!")
amt = float(input("What was the total bill? $"))
tipPerc = int(input("What % tip would you give? 10,12 or 15%? "))
people = int(input("How many people to split the bill? "))
pay = (amt + (amt*tipPerc/100))/people
print("Each person should pay: $",round(pay,2))


