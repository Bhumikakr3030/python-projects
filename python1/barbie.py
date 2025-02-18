# Barbie Text-Based Adventure Game

def start_game():
    print("Welcome to the Barbie Adventure Game!")
    print("You are Barbie, and you have a big day ahead. Let's get started!")
    print("\nYou wake up in your dream house. What do you want to do?")
    print("1. Get dressed")
    print("2. Have breakfast")
    print("3. Go outside")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        get_dressed()
    elif choice == "2":
        have_breakfast()
    elif choice == "3":
        go_outside()
    else:
        print("Invalid choice. Please try again.")
        start_game()

def get_dressed():
    print("\nYou decide to get dressed.")
    print("What outfit do you want to wear?")
    print("1. Princess dress")
    print("2. Casual outfit")
    print("3. Sportswear")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        print("\nYou look fabulous in your princess dress!")
    elif choice == "2":
        print("\nYou look stylish in your casual outfit!")
    elif choice == "3":
        print("\nYou look sporty and ready for action!")
    else:
        print("Invalid choice. Please try again.")
        get_dressed()

    print("\nNow that you're dressed, what's next?")
    print("1. Have breakfast")
    print("2. Go outside")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        have_breakfast()
    elif choice == "2":
        go_outside()
    else:
        print("Invalid choice. Please try again.")
        get_dressed()

def have_breakfast():
    print("\nYou decide to have breakfast.")
    print("What do you want to eat?")
    print("1. Pancakes")
    print("2. Fruit salad")
    print("3. Cereal")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        print("\nYou enjoy a delicious stack of pancakes!")
    elif choice == "2":
        print("\nYou have a refreshing fruit salad!")
    elif choice == "3":
        print("\nYou have a bowl of cereal!")
    else:
        print("Invalid choice. Please try again.")
        have_breakfast()

    print("\nNow that you've had breakfast, what's next?")
    print("1. Get dressed")
    print("2. Go outside")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        get_dressed()
    elif choice == "2":
        go_outside()
    else:
        print("Invalid choice. Please try again.")
        have_breakfast()

def go_outside():
    print("\nYou decide to go outside.")
    print("Where do you want to go?")
    print("1. The beach")
    print("2. The park")
    print("3. The mall")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        print("\nYou head to the beach and enjoy the sun and waves!")
    elif choice == "2":
        print("\nYou go to the park and have a picnic with friends!")
    elif choice == "3":
        print("\nYou visit the mall and do some shopping!")
    else:
        print("Invalid choice. Please try again.")
        go_outside()

    print("\nYou had a great day! Thanks for playing the Barbie Adventure Game!")
    play_again()

def play_again():
    choice = input("\nDo you want to play again? (yes/no): ").lower()
    if choice == "yes":
        start_game()
    else:
        print("Thanks for playing! Goodbye!")

# Start the game
start_game()