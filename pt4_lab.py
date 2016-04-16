import random

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi dessert")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and out run the natives.")

done = False

miles_taveled = 0
thirst = 0
camel_tiredness = 0
natives_traveled = -20
canteen = 3

while not done :
    print("\nA. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    choice = input("Your choice? : ")
    if choice.upper() == "Q":
        done = True
    elif choice.upper() == "E":
        print("\nMiles traveled:" , miles_taveled )
        print("Drinks in canteen:" , canteen  )
        print("The natives are %d miles behind you.\n" % (miles_taveled - natives_traveled))
    elif choice.upper() == "D":
        camel_tiredness = 0
        print("\n Camel is happy\n")
        natives_traveled += random.randrange(7,15)
    elif choice.upper() == "C":
        miles_taveled += random.randrange(10,21)
        print("\nMiles traveled:", miles_taveled )
        thirst += 1
        camel_tiredness += random.randrange(1,4)
        natives_traveled += random.randrange(7,15)
    elif choice.upper() == "B":
        miles_taveled += random.randrange(5, 13)
        print("\nMiles traveled:", miles_taveled)
        thirst += 1
        camel_tiredness += 1
        natives_traveled += random.randrange(7, 15)
    elif choice.upper() == "A":
        if canteen != 0:
            canteen -= 1
            thirst = 0
        else:
            print("\nthere's no water\n")
    if not done and thirst > 4 and thirst < 6:
        print("\n You are thirsty\n")
    elif thirst >6:
        print("\n You died of thirst!\n")
        done = True

    if not done and camel_tiredness >5 and camel_tiredness < 8:
        print("\n Your camel is getting tired\n")
    elif camel_tiredness > 8:
        print("\n Your camel dead.\n")
        done = True

    if miles_taveled == natives_traveled or natives_traveled > miles_taveled:
        print("\n Natives cought player.\n")
        done = True
    elif miles_taveled - natives_traveled < 15:
        print("\n The natives are getting close! \n")

    if not done and miles_taveled >= 200:
        print("\n Player Win \n")
        done = True

    if not done and 3 == random.randrange(1,13):
        print("\n OOOOOOaaaasis!!!!! \n")
        canteen = 3
        thirst = 0
        camel_tiredness = 0




# miles_taveled = 0
# thirst = 0
# camel_tiredness = 0
# natives_traveled = -20
# canteen = 15
