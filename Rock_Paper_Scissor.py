from random import randint
player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:
    print(f"Player_score: {player_wins} computer_score: {computer_wins}")
    print("..rock..")
    print("..paper..")
    print("..scissors..")

player = input("Player, make your move  ").lower()
rand_num = randint(0,2) 
if (rand_num  == 0):
    computer = "rock"
elif (rand_num  == 1):
    computer = "paper"
else:
    computer = "scissors"
    
print(f"Computer plays {computer}")

if player == computer:
    print("it's a tie")
elif player == "rock":
    if computer == "scissors ":
        print("player wins")
    elif computer == "paper ":
        print("computer wins")
elif player == "paper":
    if computer == "rock":
        print("player wins!")
    elif computer == "scissors":
        print("computer wins!")
elif player == "scissors":
    if computer == "paper":
        print("player wins")
    elif computer == "rock":
        print("computer wins")
else:
    print("Please enter a valid move")