import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while (guess != random_number):
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess == random_number:
            print(f"You guess right, the number was {guess}. You won!")
        elif guess < random_number:
            print("Sorry, you didn't guess the number, it is bigger")
        else:
            print("Sorry, you didn't guess the number, it is smaller")

def ai_guess(x):
    low, high = 1, x
    feedback = ''
    tries = 0
    while feedback != 'c':
        tries += 1
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high (H), too low (L) or correct (C)? ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Yay! The computer guessed your number, {guess}, correctly in {tries} tries!")

while True:
    game = input("Do you want to guess the AI number (1) or the AI to guess your number (2)? To exit (0) ")
    if game == '1':
        limit = int(input("Enter the upper limit of the numbers: "))
        guess(limit)
    elif game == '2':
        limit = int(input("Enter the upper limit of the numbers: "))
        ai_guess(limit)
    else:
        exit("Thanks for playing the game!")