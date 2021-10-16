#multiple ifs in roller coaster program
height = int(input("Enter your height in cm: "))
bill = 0
if height<120:
    print("Chal chote jump kar")
else:
    age = int(input("Enter your age: "))
    if age>18:
        bill+=500
    elif age<12:
        bill+=100
    else:
        bill+=300;
    pic = input("Do you want a picture? ")
    if pic is "Y":
        bill+=1000
    print("Your total bill is",bill)

   

