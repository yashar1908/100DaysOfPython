name1 = input("Enter your name: ")
name2 = input("Enter your s/o name: ")
name1 = name1.lower()
name2 = name2.lower()
tensn1 = name1.count("t")+name1.count("r")+name1.count("u")+name1.count("e")
tensn2 = name2.count("t")+name2.count("r")+name2.count("u")+name2.count("e")
onesn1 = name1.count("l")+name1.count("o")+name1.count("v")+name1.count("e")
onesn2 = name2.count("l")+name2.count("o")+name2.count("v")+name2.count("e")
tens = tensn1 + tensn2
ones = onesn1 + onesn2
love = 10*tens + ones
print("Love Percentage:",love)

