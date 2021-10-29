import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

userch = int(input("Choose 1 for rock, 2 for paper, 3 for scissors"))
userch-=1
rps = [rock,paper,scissors]
cch = random.randint(0,2)
print("You chose: \n",rps[userch])
print("Computer Chose: \n",rps[cch])
if userch==0 and cch==1: #rock and paper
    print("You Lose!")
elif userch ==1 and cch == 0: #paper and rock
    print("You Win!")
elif userch == 1 and cch == 2: #paper and scissors
    print("You Lose!")
elif userch ==2 and cch ==1: #scissors and papers
    print("You Win!")
elif userch == 2 and cch == 0: #scissors and rock
    print("You Lose!")
elif userch == 0 and cch == 2: #rock and scissors
    print("You Win!")
else:
    print("It is a draw!")