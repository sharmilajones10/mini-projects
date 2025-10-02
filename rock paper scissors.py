import random
computer=random.randint(0,2)
def game():
    r=1;user_score=0;computer_score=0
    while r<=3:
        num=int(input("press 0 for rock,1 for paper,2 for scissors"" if it is draw you have one more chance"))
        if num==computer:
            print("draw")
            print("computer choice", computer)
            continue
        if num==0:
            if computer==2:
                print("you won")
                print("computer choice",computer)
                user_score+=1
                r+=1
            else:
                print("you lost")
                print("computer choice",computer)
                computer_score+=1
                r+=1
        elif num==1:
            if computer==0:
                print("you won")
                print("computer choice", computer)
                user_score+=1
                r+=1
            else:
                print("you lost")
                print("computer choice", computer)
                computer_score+=1
                r+=1
        else:
            if computer==1:
                print("you won")
                print("computer choice", computer)
                user_score+=1
                r+=1
            else:
                print("you lost")
                print("computer choice", computer)
                computer_score+=1
                r+=1
        if r==4:
            if user_score>computer_score:
                print("you won play again")
            elif user_score==computer_score:
                print("draw")
            else:
                print("you lost better lusk next time")
    print("computer_score:",computer_score,"user_scpre:",user_score)
print(game())
