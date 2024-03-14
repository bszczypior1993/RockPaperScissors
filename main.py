import random
import time
is_on = True

print("""Welcome to a game of Rock, Paper, Scissors! 

The rules are simple: choose rock, paper, or scissors, and win or lose depending on what choice your opponent made.
ROCK beats SCISSORS
SCISSORS beat PAPER
PAPER beats ROCK""")

time.sleep(1)

def assign_choice_name(choice):
    global choice_name
    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    elif choice == 3:
        choice_name = "Scissors"
    return choice_name




def assess_result(player, computer):
    if player == computer:
        result = "draw"
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        result = "player wins"
    else:
        result = "computer wins"
    return result


player_score = 0
computer_score = 0


while is_on == True:
    player_choice = int(input("Choose 1 for ROCK, 2 for PAPER or 3 for SCISSORS. "))
    computer_choice = random.randint(1, 3)

    if player_choice not in [1, 2, 3]:
        time.sleep(1)
        print(f"Sorry! {player_choice} is not a valid choice.")
        time.sleep(1)
        player_choice = int(input("Let's try again! Choose 1 for ROCK, 2 for PAPER or 3 for SCISSORS. "))
    else:
        player_choice_name = assign_choice_name(player_choice)
        computer_choice_name = assign_choice_name(computer_choice)

    time.sleep(1)
    print(f"Your choice is {player_choice_name}.")
    time.sleep(2)
    print(f"Your opponent's choice was {computer_choice_name}.")
    time.sleep(2)

    if assess_result(player_choice, computer_choice) == "draw":
        print(f"It's a draw! \nYour score: {player_score} \nOpponent score: {computer_score}")
    elif assess_result(player_choice, computer_choice) == "player wins":
        player_score += 1
        print(f"You win! \nYour score: {player_score} \nOpponent score: {computer_score}")
    else:
        computer_score +=1
        print(f"You lose! \nYour score: {player_score} \nOpponent score: {computer_score}")

    replay = input("Play again? y/n ")
    if replay == "n":
        is_on = False
