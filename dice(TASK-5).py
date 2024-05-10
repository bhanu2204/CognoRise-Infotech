import random

def roll_dice(num_dice, num_sides):
    rolls = []
    for _ in range(num_dice):
        roll = random.randint(1, num_sides)
        rolls.append(roll)
    return rolls

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll: "))
            if num_dice <= 0:
                print("Please enter a positive number of dice.")
                continue
            num_sides = int(input("Enter the number of sides on each die: "))
            if num_sides <= 0:
                print("Please enter a positive number of sides.")
                continue
            num_rolls = int(input("Enter the number of rolls: "))
            if num_rolls <= 0:
                print("Please enter a positive number of rolls.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print("\nRolling the dice...\n")
    for i in range(num_rolls):
        rolls = roll_dice(num_dice, num_sides)
        print("Roll", i+1, ":", rolls)

if __name__ == "__main__":
    main()
