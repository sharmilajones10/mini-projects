import random
import time
print("Welcome to Rock Paper Scissors!")
print("rules:\n1)Rock beats Scissor\n2)Paper beats Rock\n3)Scissors beats Paper")
print("Choose these keys to play\n 0 for rock\n1 for paper\n2 for scissors")
def game():
    rounds=0;user_score=0;computer_score=0
    r=0
    while r<=1:
        computer = random.randint(0, 2)
        num=int(input("enter your choice:"))
        if computer==num:
            print("computer is thinking.....")
            time.sleep(2)
            print("draw")
            if computer == 0:
                print("computer choice is Rock")
            elif computer == 1:
                print("computer choice is paper")
            else:
                print("computer choice is scissors")
            r+=1
        else:
            if num==0:
                if computer==2:
                    print("computer is thinking.....")
                    time.sleep(2)
                    print("you won")
                    if computer==0:
                        print("computer choice is Rock")
                    elif computer==1:
                        print("computer choice is paper")
                    else:
                        print("computer choice is scissors")
                    r += 1

                else:
                    print("computer is thinking.....")
                    time.sleep(2)
                    print("you lost")
                    if computer==0:
                        print("computer choice is Rock")
                    elif computer==1:
                        print("computer choice is paper")
                    else:
                        print("computer choice is scissors")
                    r += 1
            elif num==1:
                if computer==0:
                    print("computer is thinking.....")
                    time.sleep(2)
                    print("you won")
                    if computer==0:
                        print("computer choice is Rock")
                    elif computer==1:
                        print("computer choice is paper")
                    else:
                        print("computer choice is scissors")
                    r += 1
                else:
                    print("computer is thinking.....")
                    time.sleep(2)
                    print("you lost")
                    if computer==0:
                        print("computer choice is Rock")
                    elif computer==1:
                        print("computer choice is paper")
                    else:
                        print("computer choice is scissors")
                    r += 1
            else:
                if computer==1:
                    print("computer is thinking.....")
                    time.sleep(2)
                    print("you won")
                    if computer==0:
                        print("computer choice is Rock")
                    elif computer==1:
                        print("computer choice is paper")
                    else:
                        print("computer choice is scissors")
                    r += 1
                else:
                    print("computer is thinking.....")
                    time.sleep(2)
                    print("you lost")
                    if computer==0:
                        print("computer choice is Rock")
                    elif computer==1:
                        print("computer choice is paper")
                    else:
                        print("computer choice is scissors")
                    r += 1
        again=input("Do you want to play again? \nsay y or n")
        if again=="y" or "n":
            if again=="y":
                print("Choose these keys to play\n 0 for rock\n1 for paper\n2 for scissors")
                print(game())
            else:
                print("Thank you for playing")
                break
        break
print(game())
