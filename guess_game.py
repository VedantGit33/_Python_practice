import random

print('Hello! Welcome to the game!')
print("I'm thinking of a number")
print("Let's see if you able to guess it right!")

secret_number = random.randint(1,100)

attempts = 0
guess = 0

while guess!=secret_number:

    try:
        guess = int(input("Enter your guess:"))
        attempts+=1


        if guess < secret_number:
            print("Too low! Give it another try.")

        elif guess > secret_number:
            print("Too high! Give it another try")

        else:
            print(f"Congratulations!!!! You've guess the number in {attempts} attempts.")

    except ValueError:
        print("Invalid input! Enter a valid number")

print("Thanks for playing")
