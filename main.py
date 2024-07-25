from getpass import getpass
import random

# Welcome message
print("Snake Water Gun Game\n".center(70))

# Options for the game
print("Put the letter T/C/E in upper case")
choice = input("T for Two Player, C for Computer, E for Exit. Select T/C/E: ").upper()

if choice == 'T':
    # Two-player mode
    user1 = getpass("\nUser 1 Choose Snake/Water/Gun: ").lower()
    user2 = getpass("\nUser 2 Choose Snake/Water/Gun: ").lower()

    print("\nUser 1:", user1)
    print("User 2:", user2)

    if user1 == user2:
        print("\nGame ended in a draw.")
    elif (user1 == "snake" and user2 == "water") or (user1 == "water" and user2 == "gun") or (user1 == "gun" and user2 == "snake"):
        print("\nUser 1 won the game.")
    else:
        print("\nUser 2 won the game.")

elif choice == 'C':
    # Computer mode
    user = getpass("\nUser Choose Snake/Water/Gun: ").lower()
    print("User:", user)

    options = ["snake", "water", "gun"]
    comp = random.choice(options)
    print("Computer:", comp)

    if user == comp:
        print("\nGame ended in a draw.")
    elif (user == "snake" and comp == "water") or (user == "water" and comp == "gun") or (user == "gun" and comp == "snake"):
        print("\nUser won the game.")
    else:
        print("\nComputer won the game.")

elif choice == 'E':
    print("\nExiting from the game.")
else:
    print("\nInvalid choice. Exiting from the game.")
