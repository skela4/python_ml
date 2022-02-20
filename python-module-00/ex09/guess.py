from random import randint
import string


def intro():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 ", end="")
    print("to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!\n")


def guess():
    intro()
    found = 0
    attempt = 1
    num_to_guess = 42
    # num_to_guess = randint(1, 99)
    while found == 0:
        number = input("What's your guess between 1 and 99?\n")
        if number == 'exit':
            print("Goodbye!")
            exit(1)
        try:
            number = int(number, 10)
        except Exception:
            print('not a valid number')
            attempt += 1
            continue
        if number == num_to_guess:
            if num_to_guess == 42:
                print("The answer to the ultimate question of life,", end="")
                print(" the universe and everything is 42")
            if attempt == 1:
                print("Congratulations, you've got it on your first try!")
                exit(1)
            print("Congratulations, you've got it!")
            print(f"You won in {attempt} attempts!")
            exit(1)
        elif number < num_to_guess:
            print("Too low!")
        elif number > num_to_guess:
            print("Too high!")
        attempt += 1


if __name__ == "__main__":
    guess()
