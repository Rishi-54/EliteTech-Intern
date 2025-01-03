import random

def roll_dice():
    """Return a random number between 1 and 6, simulating a dice roll."""
    return random.randint(1, 6)

def main():
    """Run the dice roll simulator."""
    print("Welcome to the Dice Roll Simulator!")

    while True:
        input("\nPress Enter to roll the dice...")
        print(f"You rolled: {roll_dice()}!")

        play_again = input("Roll again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("\n Thanks for playing!")
            break

if __name__ == "__main__":
    main()
