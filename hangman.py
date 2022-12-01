import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    print(word)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6
    while len(word_letters) > 0 and lives > 0:
        # Show the letters already used to the player
        print("You have ", lives, " lives left. You have used there letters: ", ' '.join(used_letters))
        # What is the current word with "-" where the letters are not discovered
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))
        # Get the player input
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("The letter is not in the word.")
        elif user_letter in used_letters:
            print("You have already used that character, please try again.")
        else:
            print("Invalid character, please try again.")
    if lives == 0:
        print("You died! The word was ", word)
    else:
        print("Congrats! You won!")
hangman()