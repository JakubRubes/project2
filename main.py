"""
projekt_2.py: Second project, Bulls and Cows game

author: Jakub Rubes
email: rubes.jakub@email.cz
"""
import random
initial_game_text = '''
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------
'''
print(initial_game_text)

def generate_unique_4digit():
    first_digit = random.choice(range(1, 10))  # 1–9 only
    remaining_digits = random.sample([d for d in range(10) if d != first_digit], 3)
    digits = [first_digit] + remaining_digits
    return int(''.join(map(str, digits)))

def has_unique_digits(number):
    number_to_string = str(number)
    return len(number_to_string) == len(set(number_to_string))

guessed_number = (input())  # capturing user input value

match guessed_number:
    case num if num.isdigit() == False:  # is it only numbers
        print("Enter numbers ONLY.")
    case num if len(num) != 4:  # is length 4
        print("Your number is not 4 digit.")
    case num if num[0] == "0":  # isn't first digit 0
        print("First digit cannot be 0.")
    case num if not has_unique_digits(num):  # are digits unique
        print("Enter number without repeating digits.")
    case _:
        print("Valid number.")  #  variable for valid guess
        valid_number = int(guessed_number)
    
unique_number = generate_unique_4digit()  # variable for generated number

