#nested if means one if statement inside another 
#WAP to modify rollercoaster program if age>18 then price 500rs else 200rs

height = int(input("Enter your height in cm: "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You have to pay Rs. 500 for the ticket.")
    else:
        print("You have to pay Rs. 200 for the ticket.")
else:
    print("Chal chote jump kar!")

