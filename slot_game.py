# It's a casino slots game. has three wheels and has ["🍒", "🍋", "7️⃣", "⭐"] symbols.
# enter your bet amount and spin the wheels.
# if you get ⭐⭐⭐ its a jackpot you will get 1000 points
# if you get 7️⃣7️⃣7️⃣ you will get 100 pts
# if you get 🍋🍋🍋 you will get 50 pts
# if you get 🍒🍒🍒 you will get 20 pts
## if you get any two same you will get 5 pts
# if you get all three diffrent you will get 300 pts deducted
import random
import sys
bet=int(input("Place your bet "))
symbols = ["🍒", "🍋", "7️⃣", "⭐"]
probabilities = [0.5, 0.3, 0.15, 0.05]
def get_fr():
    return random.choices(symbols, weights=probabilities, k=1)[0]

start=input("press's'to start the game ")
while start=="s":
    game=input("enter'r' to roll or 'e' to exit ")
    if game=="e":
        print("exited with your current bet",bet)
        sys.exit()      
    else:
        pass
        result1 = get_fr()
        result2 = get_fr()
        result3 = get_fr()
        if bet<0:
            print("you lost all LOL you can't play anymore, refill the bet, your current score is ",bet)
            sys.exit()
        elif result1==result2==result3=="⭐":
            bet+=1000
            print("Jackpot! you got",result1,result2,result3, "Your new bet is:", bet)
        elif result1==result2==result3=="7️⃣":
            bet+=100
            print("You won! you got",result1,result2,result3, "Your new bet is:", bet)
        elif result1==result2==result3=="🍋":
            bet+=50
            print("You won! you got",result1,result2,result3, "Your new bet is:", bet)
        elif result1==result2==result3=="🍒":
            bet+=20
            print("You won! you got",result1,result2,result3, "Your new bet is:", bet)
        elif (result1==result2) or (result1==result3) or (result3==result2):
            bet+=5
            print("You won! you got",result1,result2,result3, "Your new bet is:", bet)
        else:
            bet-=300
            print("You lost! you got",result1,result2,result3, "Your new bet is:", bet)
    

        