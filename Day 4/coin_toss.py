#WAP to randomize a coin toss and return heads or tails
import random
toss = random.randint(0,1)
if toss == 0:
    print("Heads")
else:
    print("Tails")
