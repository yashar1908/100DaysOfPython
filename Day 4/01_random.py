#en.wikipedia.org/wiki/Mersenne_Twister
#askpython.com

import random 

#I.To generate a random number between a and b (both inclusive)
#random.randint(start,end)
print(random.randint(100,200))


#II. To generate random  number in a range witha given step condition
#random.randrange(start,stop,step)
#suppose you want a random 3 digit even number, so you'll use this function as below:
# r_even_no = random.randrange(100,1000,2) the step is the number of integers it has to jump
#for example, the below line should only output either 5 or 10.
print(random.randrange(5,12,5)) 
#logic is that it has to start at 5 and it can only step up 5 numbers so it can go 5/10 and nothing else

#III. Random number between [0.0,1.0): random.random()
print(random.random())

'''
random.randint(a,b) - inclusive
random.randrange(a,b,step) - a, a+step, a+2*step, .... b (b not necessarily included)
random.random() -  floating point number between 0 and 1 (1 not inclusive)

'''
#Generating a random floating point number between 0 and n, say 7
#we know that random.random() gives between 0 and 1 so if we multiply it by 7 we will get betwwen 0 and 7
rand_float01 = random.random()
rand_float07 = 7 * rand_float01
print(rand_float07)

