import game_data
import random;

hasGuessed = True;
score = 0;

def display(player):
    print(f"{player['name']}, {player['description']}, from {player['country']}");
    
def choose_player():
    player = random.choice(game_data.data);
    game_data.data.remove(player);
    return player;
first = choose_player();

def check_answer(first, second, answer):
    if answer == 'A':
        if first['follower_count'] > second['follower_count']:
            return True;
        else:
            return False;
    elif answer == 'B':
        if second['follower_count'] > first['follower_count']:
            return True;
        else:
            return False;


while hasGuessed:
    second = choose_player();
    print("Compare A:", end = ' ');
    display(first);
    print("\n\n\n\n\nAgainst B:", end = ' ');
    display(second);
    answer = input("Who has more followers? Type 'A' or 'B': ");
    hasGuessed = check_answer(first,second,answer);
    if hasGuessed:
        score += 1;
        print("You're Right! Current Score:",score);
    else:
        print("That's Wrong. Your final score:",score);
        break;
    first = second;
    
