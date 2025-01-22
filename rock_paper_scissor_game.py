import random

print("Welcome to Rock,Paper and Scissors")

choices = ['rock','paper','scissor']

user_choice = input("Please choose between (rock,paper,scissor):").lower()

if user_choice not in choices:
    print("Invalid Choice! Fuckinnn choose between (rock,paper,scissor)")

else :
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        print("It's a tie.")

    elif (user_choice=='paper' and computer_choice=='rock') or \
    (user_choice=='scissor' and computer_choice=='paper') or \
    (user_choice=='rock' and computer_choice=='scissor'):

        print("Conrats! You won.")

    else :
        print("You Lost :))")

print("Thanks for playing")
