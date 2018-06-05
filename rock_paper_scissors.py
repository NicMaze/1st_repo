from random import randint

print("...rock...")
print("...paper...")
print("...scissors...")
player_score = 0
computer_score = 0
while (player_score <= 4) and (computer_score <= 4):
    player = input("Type your choice of rock, paper, scissors: ").lower()
    if player == "q" or player == "quit":
        break
    rand_num = randint(0, 2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print("Computer choice: " + computer)
    if player[0] == computer[0]:
        print("draw")
    elif player[0] == "r" and computer[0] == "s":
        print("player 1 wins!!!")
        player_score += 1
    elif player[0] == "p" and computer[0] == "r":
        print("player 1 wins!!!")
        player_score += 1
    elif player[0] == "s" and computer[0] == "p":
        print("player 1 wins!!!")
        player_score += 1
    else:
        print("Computer Wins!!")
        computer_score += 1
    print(f"{player_score} vs {computer_score}")

if player_score == 5:
    print("CONGRATULATIONS!! You boss son of a bitch")
else:
    print("Sorry, so close...")
