# It's an good prank to play with user to give them a interactive feeling with app
input("enter to proceed")
name=input("your name")
print("welcome",name)
a=int(input("type your password (hint- your password is 123"))
if(a==123):
    print("wrong password, did you really think i'll give the password so easily try something different")
    b=int(input("type your password"))
    if(b==123):
        print("really!!!! ")
        print("trying the same password again")
        input("press enter if you want to proceed with same password")
        print("oh you're smart you didn't fall for the trap")
        print("recognition complete, you may enter")
        input("enter  to continue")
    else:
            print("psych, that's the wrong password.")
            print("Security breach detected... Initiating lockdown sequence!")
            input("enter  to save you're life")
            print(" Your 1st password was correct i was just kidding")
            print("recognition complete, you may enter")
            input(" enter  to continue")
else:
    print("incorrect password")
    print("Security breach detected... Initiating lockdown sequence!")
    input("enter to save your life")

    print("your life has been spared try again")
