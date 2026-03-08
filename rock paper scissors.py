import random
def game():
    rounds=0;user_score=0;computer_score=0
    print("Welcome to Rock Paper Scissors!")
    print("rules:\n1)Rock beats Scissor\n2)Paper beats Rock\n3)Scissors beats Paper")
    print("Choose these keys to play\n 0 for rock,1 for paper,2 for scissors")
    while rounds <= 2:
        computer = random.randint(0, 2)
        num=input("enter your choice:")
        if num==computer:
            print("draw")
            rounds+=1
        if num==0:
            if computer==2:
                print("computer choice:", computer)
                print("you won")
                user_score+=1
                rounds+=1
            else:
                print("computer choice:", computer)
                print("you lost")
                computer_score+=1
                rounds+=1
        elif num==1:
            if computer==0:
                print("computer choice:", computer)
                print("you won")
                user_score+=1
                rounds+=1
            else:
                print("computer choice:", computer)
                print("you lost")
                computer_score+=1
                rounds+=1
        else:
            if computer==1:
                print("computer choice:", computer)
                print("you won")
                user_score+=1
                rounds+=1
            else:
                print("computer choice:", computer)
                print("you lost")
                computer_score+=1
                rounds+=1
        if rounds==3:
            if user_score > computer_score:
                print("you won this game")
            elif user_score == computer_score:
                print("draw match")
            else:
                print("you lost better lusk next time")
    print("\ncomputer_score:",computer_score,"\nuser_score:",user_score)
    again=input("Do you want to play again? \nsay yes or no")
    if again=="yes":
        print(game())
    else:
        print("Thank you for playing")
print(game())
