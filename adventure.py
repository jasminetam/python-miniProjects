name = input("Type your name: ")
print("Welcome", name, "to this adventure!");

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across (walk/swim)? ").lower()
    if answer == "swim":
        print("You swim across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
    if answer == "back":
        print("You go back and meet a robber, you are dead.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ").lower()
        if answer == "yes":
            print("You talk to the stranger and they lead to a treasure. You win!")
        elif answer == "no":
            print("You ignore the stranger and go into a dark forest, walk until dead.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
   
else: 
    print("Not a valid option. You lose.")

print("Thank you for trying", name)