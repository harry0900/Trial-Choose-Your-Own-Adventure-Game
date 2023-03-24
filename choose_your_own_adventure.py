import random

# Player's name
name = input("What is your name? ")

# Player's initial stats
health = 100
magic = 50
weapon = None

# Introduction
print(f"Welcome, {name} the Mighty! You are in a mysterious land. Are you ready to discover the secrets within?")


# Main game loop
while True:
    # Present options
    print("\nYou find yourself in the middle of a clearing. There is a forest to the North, \na cave to the South, and a town to the East. What do you want to do?")
    print("1. Explore the forest")
    print("2. Enter the cave")
    print("3. Go to the town")
    print("4. Check your inventory")
    print("5. Quit the game")

    # Get player's choice
    choice = input("Enter the number of your choice: ")

    # Handle the player's choice
    if choice == "1":
        print("You enter the dense forest. You hear the sounds of wildlife around you.")
        print("Suddenly, you are attacked by a band of goblins!")
        if weapon:
            print(f"You draw your {weapon} and fight off the goblins. You take some damage but emerge victorious.")
            health -= random.randint(10, 20)
        else:
            print("You try to fight the goblins with your bare hands, but they overwhelm you. You take heavy damage.")
            health -= random.randint(30, 40)

        print(f"You run back to the clearing. Your current stats are: Health = {health}, Magic = {magic}")
        if weapon:
            print(f"You are wielding a {weapon}.")
        else:
            print("You don't have any weapon.")

        # Check if the player is still alive
        if health <= 0:
            print("You have died. Game over.")
            break

    elif choice == "2":
        print("You enter the dark cave. The air is damp and chilly.")
        print("You hear strange whispers and footsteps echoing through the cave.")
        print("As you move further in, you see a glowing crystal.")
        print("Do you touch it?")
        touch_choice = input("Enter 'yes' or 'no': ")
        if touch_choice == "yes":
            print("You touch the crystal and feel a surge of magic flowing through you.")
            print("You gain some magic points.")
            magic += random.randint(10, 20)
        else:
            print("You decide not to touch the crystal and continue exploring the cave.")

        print("You encounter a dragon! It breathes fire at you.")
        if magic > 50:
            print("You use your magic to deflect the dragon's fire back at it. The dragon takes damage and flies away.")
        else:
            print("You try to dodge the dragon's fire but get hit. You take heavy damage.")
            health -= random.randint(30, 40)

        print(f"You decide to go back to the clearing. Your current stats are: Health = {health}, Magic = {magic}")
        if weapon:
            print(f"You are wielding a {weapon}.")
        else:
            print("You don't have any weapon.")

        # Check if the player is still alive
        if health <= 0:
            print("You have died. Game over.")
            break

    elif choice == "3":
        print("You enter the bustling town. People are busy with their daily activities.")
        print("You hear rumors about a cursed sword hidden in the nearby ruins.")
        print("Do you want to go to the ruins?")
        ruins_choice = input("Enter 'yes' or 'no': ")
        if ruins_choice == "yes":
            print("You arrive at the ruins and find the cursed sword.")
            print("Do you pick it up?")
            sword_choice = input("Enter 'yes' or 'no': ")
            if sword_choice == "yes":
                print("You pick up the cursed sword and feel its power coursing through you.")
                print("You gain a powerful weapon, but it comes at a cost.")
                weapon = "cursed sword"
                health -= 20
            else:
                print("You decide not to pick up the cursed sword and leave the ruins.")
        else:
            print("You decide the town is not worth it and you go back to the clearing.")


    elif choice == "4":
        print(f"You check your inventory. You find a hidden herb and eat it. Your wounds start healing.")
        heal_points = random.randint(10, 20)
        health = min(health + heal_points, 100)
        print(f"You heal {heal_points} points. Your current health is {health}.")
        print(f"Your current magic is {magic}")
        if weapon:
            print(f"You are wielding a {weapon}.")
        else:
            print("You don't have any weapon.")



    elif choice == "5":
        print("Thank you for playing the game!")
        break


    else:
        print("Invalid choice. Please enter a valid option.")

print(f"Game over, {name}. Your final stats are: Health = {health}, Magic = {magic}")

if weapon:
    print(f"You were wielding a {weapon}.")
