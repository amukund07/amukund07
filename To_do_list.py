# # timer list
# import time
# a=input("Choose your task or type exit to end = ")
# b=int(input("time alloted= "))
# i=b
# print("do your task",a)
# while i>=0:
#     time.sleep(1)
#     print(i)
#     i-=1
# print ("task complete")

# advanced timer list
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
print("exited")
