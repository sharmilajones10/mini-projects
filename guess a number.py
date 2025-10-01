import random
import numpy as np
secret_number=random.randint(1,10,)
def guessing_number():
        chances=1
        while chances<=3:
            num=int(input("enter a number"))
            if num==secret_number:
                print("you won")
                break
            else:
                print("try again")
            chances+=1
            if chances == 4:
                print("you lost")
                break
print(guessing_number())
