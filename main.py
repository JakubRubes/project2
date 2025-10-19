"""
projekt_2.py: Second project, Bulls and Cows game

author: Jakub Rubes
email: rubes.jakub@email.cz
"""
import random

def initial_game_text():
    print("""
    Hi there!
    -----------------------------------------------
    I've generated a random 4 digit number for you.
    Let's play a bulls and cows game.
    -----------------------------------------------
    Enter a number:
    -----------------------------------------------
    """)

def generate_unique_4digit():
    # Returns the unique 4-digit number that does not start with "0" as a string.
    first_digit = random.choice(range(1, 10))  # 1–9 only
    remaining_digits = random.sample([d for d in range(10) if d != first_digit], 3) # 0-9 unique
    digits = [first_digit] + remaining_digits
    return ''.join(map(str, digits))

def correct_guess(raw_guess):
    # Loops until the user provides a valid 4-digit guess
    while True:
        num = str(raw_guess)     
        # Validation checks
        if not num.isdigit():
            print("Enter numbers ONLY!")
        elif len(num) != 4:
            print("Enter exactly 4 digits!")
        elif num[0] == "0":
            print("First digit cannot be 0!")
        elif not has_unique_digits(num):
            print("Enter number without repeating digits!")
        else:
            return num       
        raw_guess = input("Enter a valid 4-digit number: ")

def has_unique_digits(number):
    # Checks if a string or number has unique digits
    number_to_string = str(number)
    return len(number_to_string) == len(set(number_to_string))
    
def bulls_and_cows(guessed_number_str, generated_number_str):
    # Count Bulls and Cows
    bulls = 0
    cows = 0  
    # Check for Bulls (correct digit and correct position)
    for i in range(4):
        guess_digit = guessed_number_str[i]
        
        if guess_digit == generated_number_str[i]:
            bulls += 1
        # Check for Cows (correct digit but wrong position)
        elif guess_digit in generated_number_str:
            cows += 1          
    return (bulls, cows)

def singular_or_plural(bulls, cows):
    # Returns the correct plural/singular string for Bulls and Cows
    bull_string = "bull" if bulls == 1 else "bulls"
    cow_string = "cow" if cows == 1 else "cows"
    return (bull_string, cow_string)

def guess_evaluation(bulls, cows, bull_string, cow_string):
    # Prints the result of the current turn
    if bulls < 4: 
        print(f"Result: {bulls} {bull_string}, {cows} {cow_string}")
    # The final "GGs, you have won!" is handled by the main game loop's final print.

def game():
    # Main game body
    initial_game_text()   
    generated_number = generate_unique_4digit()    
    guess_count = 0
    bulls = 0
    # Main Game loop (continues until 4 bulls are achieved)
    while bulls < 4:    
        raw_guess = input("Enter your guess: ")     
        # Get and validate the guess
        guessed_number = correct_guess(raw_guess)    
        guess_count += 1      
        # Calculate scores
        bulls, cows = bulls_and_cows(guessed_number, generated_number)    
        # Prepare result strings
        bull_string, cow_string = singular_or_plural(bulls, cows)    
        # Display turn result
        guess_evaluation(bulls, cows, bull_string, cow_string)
        print("-----------------------------------------------")      
    # Final Win Message
    print(f"GGs, you have won! You cracked the code {generated_number} in {guess_count} guesses!")
# To ensure that game does not run automatically if someone wants to import this file and run only random function.
if __name__ == "__main__":
    game()