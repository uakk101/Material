import random

def play_game(secret_number, max_guesses):
    print("Guess the number between 1 and 100!")

    for _ in range(max_guesses):
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number!")
            return

    print("Game over! The number was", secret_number)
    
secret_number = random.randint(1, 100)
max_guesses = 5


play_game(secret_number, max_guesses)
