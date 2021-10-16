#String
name = "Yash Arora"
#print(name)

#character 
gender = 'M'
# print(gender)

#Integer
age = 19
# print(age)

#for the sake of convenience, python allows putting underscores in integer values for easier understanding
netWorth = 352_192_000_000_000
#print(netWorth) #output is 352192000000000 and not 352_192_000_000_000.
#does not allow commas though. only underscores. the underscores are ignored while executing 

#float
percentile = 91.157
# print(percentile)

#underscores allowed for float as well.
nationalDebt = 312_532_679.879
#print(nationalDebt) #outputs 312532679.879

#boolean
hindu = False #F capital
awake = True  #T capital
#print(hindu)
#print(awake)

#String is a collection of characters and can be treated as an array 
name1 = name[0] #stores Y

#Basic String slicing:
name2 = name[0:2] #stores YA [lower limit,upper limit)
#print(name2)

name3 = name[1:] #stores all characters from 1 to end of string (lower limit inclusive)
#print(name3)

name4 = name[:6] #prints from 0 to n-1 (upper limit excluded)
#print(name4)