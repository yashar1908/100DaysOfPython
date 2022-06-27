import random

print("Welcome to the Number Guessing Game!");

print("I'm thinking of a number between 1 and 100.");
number = random.randint(1,100);

difficulty = input("Choose a difficulty: 'easy' or 'hard' ");

if difficulty == 'easy':
    chances = 10;
elif difficulty == 'hard':
    chances = 5;
else:
    print("Choose a correct difficulty.");

guessed = False;

while not guessed:
    print("You have",chances,"attempts remaining to guess the number.");
    guess = int(input("Make a guess: "));
    if guess > number:
        print("Too high.");
    elif guess < number: 
        print("Too low.");
    else:
        guessed = True;
        print("You have guessed the number!!");
        break;
    chances -= 1;
    if chances == 0:
        print("You've run out of guesses. You Lose.");
        break;
    print("Guess again.");

