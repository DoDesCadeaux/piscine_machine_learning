from random import randint


def welcome():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number")
    print("Type 'exit' to quit the game")
    print("Good luck!")


def generate_random() -> int:
    return randint(1, 99)


def game():
    answer = generate_random()
    attempts = 0
    while True:
        try:
            guess = input("What's your guess between 1 and 99?\n")
            if guess == "exit":
                print("Goodbye")
                exit(0)
            elif type(int(guess)) is not int:
                raise ValueError
        except ValueError:
            print("That's not a number.")
            continue
        attempts += 1
        if int(guess) == answer:
            if answer == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            if attempts != 1:
                print("Congratulations, you've got it!")
            if attempts == 1:
                print("Congratulations! You got it on your first try!")
            else:
                print(f"You won in {attempts} attemps")
            exit(0)
        elif int(guess) > answer:
            print("Too high!")
            continue
        elif int(guess) < answer:
            print("Too low!")
            continue


def main():
    welcome()
    game()


if __name__ == "__main__":
    main()
