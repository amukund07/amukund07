snacks = [
    {"id": 1, "name": "Lays Chips", "price": 30},
    {"id": 2, "name": "KitKat", "price": 25},
    {"id": 3, "name": "Pepsi", "price": 35},
    {"id": 4, "name": "Oreo", "price": 20},
    {"id": 5, "name": "Snickers", "price": 30},
    {"id": 6, "name": "Doritos", "price": 45},
    {"id": 7, "name": "Bisleri Water", "price": 20},
    {"id": 8, "name": "Muffin", "price": 50},
    {"id": 9, "name": "Cold Coffee", "price": 60}
]

wins = {
    1: 30,
    2:25,
    3: 35,
    4: 20,
    5:30,
    6:45,
    7:20,
    8:50,
    9:60}


for s in snacks:
    print(s)


a=int(input("select your sacks ").lower())

b=int(input("Your money "))

if wins[a]==b:
    print("transaction complete")
elif wins[a]<b:
    print("Input amount= ",b)
    print("Snacks price= ",wins[a])
    print("Tranaction complete take the reamaing amount",b-wins[a])
else:
        print("put more money")