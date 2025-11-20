import random
a=input("Choose rock,paper or scissors ").lower()
w=["rock",'paper',"scissors"]
def sign():
    return random.choice(w)
c=sign()
wins = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}
if a==c:
    print("computer choice was", c," ; result tie")
elif wins[a]==c:
    print("computer choice was", c," ; result player wins")
else:
    print("computer choice was", c," ; result computer wins")
