#program to check if a year is a leap year
year = int(input("Enter a year: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap Year.")
        else:
            print("Not a leap year.")
    else:
        print("Leap Year")
else:
    print("Not a leap year")