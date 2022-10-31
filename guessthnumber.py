import random


def guess(x):
    random_number = random.randint(1, x)
    guess_num = 0
    while guess_num != random_number:
        guess_num = int(input(f'Guess a number between 1 and {x}: '))
        if guess_num < random_number:
            print("Guess again, Too low.")
        elif guess_num > random_number:
            print("Guess again, Too high.")

    print(f"Yay you have guessed the number {random_number}, Congrats!!")


guess(100)
