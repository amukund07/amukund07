# A multiplayer game can be played b/w 2-4 players .
# Simple set of rules every player will get chance to roll respectively ,will get outcome from 1 to 6.
# if the player get 1 its score becomes 0 if player gets any number other than 1  it will get added into players score.
# 1st one to reach 100 wins the game
import random
import sys
def get_num():
    return random.randint(1,6)
a=input("Enter's' to START or 'e' to EXIT ").lower()
n=int(input("choose number of player b/w 2 to 4 "))
l=[0,0,0,0,0] 
if a=="s":
    while True:
        d1=input("do you want to roll the dice or exit"
                    "press'r'to ROLL or 'e' to EXIT ").lower()
        if d1!="r":
            print("Exited")
            sys.exit()
        else:
            for i in range(1,n+1):
                d2=input(f"Player {i} press enter to roll")
                b= get_num()

                if b!=1:
                    l[i]=b+l[i]
                    print(f"player {i} got", b," your current score is= ",l[i])   
                
                else:
                    l[i]-=l[i]
                    print(f"LOL player {i} got ",b,"your current score is= ",l[i])
                
                if l[i] >= 100:
                    print(f"Player {i} won the game! 🏆")
                    sys.exit()
