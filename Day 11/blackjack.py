import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10];
computerWin = False;
userWin = False;
Draw = False;

def blackjack(hand):
    sum = 0
    for card in hand:
        sum += card;
    if sum == 21:
        return True;
    else:
        return False;


userHand = [random.choice(cards), random.choice(cards)];
computerHand = [random.choice(cards), random.choice(cards)];
userScore = userHand[0]+userHand[1];
computerScore = computerHand[0]+computerHand[1];

print("Your cards:",userHand);
print("Current Score:", userScore);
print("Computer's first card:",computerHand[0]);

if blackjack(computerHand):
    print("Computer hit BlackJack! Computer has won.");
    computerWin = True;
elif blackjack(userHand):
    print("You hit BlackJack! You win!");
    userWin = True;


while not computerWin and not userWin and not Draw:
    
    while computerScore <= 16:
        computerCard = random.choice(cards);
        computerScore += computerCard;
        computerHand.append(computerCard);
    
    anotherCard = input("Type y to get another card, type n to pass. ");
    if anotherCard == 'y':
         newCard = random.choice(cards);
         
         if(newCard == 11 and userScore + newCard > 21):
            newCard = 1;
         
         userHand.append(newCard);
         userScore += newCard;
         print("Your cards:",userHand);
         print("Current Score:", userScore);
         print("Computer's first card:",computerHand[0]);
    
    if blackjack(computerHand):
        print("Computer hit BlackJack! Computer has won.");
        computerWin = True;
        break;
    elif blackjack(userHand):
        print("You hit BlackJack! You win!");
        userWin = True;
        break;

    if anotherCard == 'n':
        print("Your final hand:",userHand);
        print("Your final score:",userScore);
        print("Computer's final hand:",computerHand);
        print("Computer's final score:",computerScore);
        if computerScore > userScore:
            computerWin = True;
            print("Computer's final score is higher than your final score. You lose.");
            break;
        elif userScore > computerScore:
            userWin = True;
            print("You win!");
            break;
        else:
            Draw = True;
            print("It is a draw.");
            break;
    
    if userScore > 21:
        computerWin = True;
        print("You went over. You lose.");
        break;