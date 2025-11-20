# advanced timer list in which until you don't want to stop it can ask for task on its own
# until you dont complete your task it will ask you to do again

c=input("enter s to start or e to exit= ").lower()
while c=="s":
    import time
    a=input("Choose your task or type exit to end = ").lower()
    import sys
    if a=="exit":
        print("exited")
        sys.exit()
    x=int(input("Choose the countdown time(in hours) "))
    y=int(input("Choose the countdown time(in minutes) "))
    z=int(input("Choose the countdown time(in seconds) "))
    i=x*3600+y*60+z
    print("do your task",a)
    while i>=0:
        time.sleep(1)
        print(i)
        i-=1
    d=input("Did you completed task, YES OR NO = ").lower()
    if d=="yes":
        print ("task complete")
    elif d=="no":
        print("Do the task again")
    else:
        print("invalid input")  
    while d=="no":
         x=int(input("Choose the countdown time(in hours) "))
         y=int(input("Choose the countdown time(in minutes) "))
         z=int(input("Choose the countdown time(in seconds) "))
         i=x*3600+y*60+z
         print("do your task",a)
         while i>=0:
            time.sleep(1)
            print(i)
            i-=1
         d=input("Did you completed task, YES OR NO = ").lower()
print("exited")

