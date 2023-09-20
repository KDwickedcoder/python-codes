choice1 = input('you have come to a crossraod. Where do you want to go "left" or "right"\n').lower()
if choice1 == "left":
    choice2 = input('you have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat or "swim" to swim across\n').lower()
    if choice2 == "wait":
        choice3 = input('you have come to the island. There is a house with 3 doors red, yellow and blue. Which colour do you want to choose\n').lower()
        if choice3 == "red":
            print("Burned by fire. Game Over")
        elif choice3 == "blue":
            print("Eaten by Beasts. Game Over")
        elif choice3 == "yellow":
            print("You Win")
        else:
            print("Game Over")
    else:
         print("Attacked by a Trout. Game Over") 
else:
    print("Fall into a hole. Game Over")












