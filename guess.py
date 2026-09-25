import random

while True:
    secret = random.randint(1, 100)
    tries = 0
    max_tries = 7

    print("Guess a number between 1 and 100")

    while tries < max_tries:
        guess = int(input("Your guess: "))
        tries = tries + 1

        if guess < secret:
            print("Too low")
        elif guess > secret:
            print("Too high")
        else:
            print("Congratulations! You found it in", tries, "tries")
            break
    else:
        print("Game over! The number was", secret)

    again = input("Play again? (yes/no): ")
    if again != "yes":
        break

print("Thanks for playing!")