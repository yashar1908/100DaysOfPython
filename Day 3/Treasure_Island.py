print("Welcome to treasure island!")
choice = input("Make a choice...Right or left? ")
if choice == "left":
    choice = input("Make a choice...swim or wait? ")
    if choice == "swim":
        print("Attacked by trout. Game over.")
    if choice == "wait":
        choice = input("Which door? Red/Blue/Yelloww? ")
        if choice == "red":
            print("Burned by fire. Game over")
        elif choice == "blue":
            print("Eaten by beasts. Game over.")
        elif choice == "yellow":
            print("You win!")
        else:
            print("ara bahy par tu ha kon?")
else:
    print("Fall into a hole. Game Over.")


