import random
print("1.rock\n2.scissor\n3.paper")
user = float(input("choose rock,scissors,paper:"))
game = random.randrange(0,3)
if user > 3 or type(user) != float:
    print("\nInvalid input, type again ")
while user != 1 and user != 2 and user != 3:
    print("\n1.rock\n2.scissor\n3.paper")
    user = float(input("choose rock,scissors,paper:"))

#user
if user == 1:
    person = "rock"
elif user == 2:
    person = "scissors"
else:
    person = "paper"

#computer
if game == 0:
    computer = "rock"
elif game == 1:
    computer = "scissors"
else:
    computer = "paper"
print("Your Choice:",person)
print("Computer's Choice:",computer)

#versus
if user =="rock":
    if computer == "rock":
        print("Draw")
    elif computer == "paper":
        print("You Lose")
    else:
        print("You win")
elif user == "paper":
    if computer == "rock":
        print("You win")
    elif computer == "paper":
        print("Draw")
    else:
        print("You Lose")
else:
    if computer == "rock":
        print("You Lose")
    elif computer == "paper":
        print("You win")
    else:
        print("Draw")