#Pizza order program
bill = 0
size = input("What size pizza do you want? (s/m/l) ")
if size is "S" or "s":
    bill+=1000
elif size is "M" or "m":
    bill+=2000
elif size is "L" or "l":
    bill+=3000
else:
    print("Ara bahy par tu ha kon?")

pep = input("Nigga you want dat pepperoni? ")
if pep is "Y" or "y":
    bill+=669
cheese = input("And what 'bout sum o'dat cheese? ")
if cheese is "Y" or "y":
    bill+=0.96

print("Your total bill value is:",bill)