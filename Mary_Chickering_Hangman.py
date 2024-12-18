""""
┌───────────────────────────────────────────────────────────────────────────┐
│                                 Hangman                                   │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: Mary Chickering                                                     │
│ Log: Finished project (1.0)                                               |
| Bugs: N/K                                                                 │
│ Description: User may guess the letters of an unknown randomly generated  |
| word. For each wrong guess, a new line on the stick figure is printed.    |
| When the stick figure is full and they still have not guessed the word,   |
| the user loses                                                            |                             
└───────────────────────────────────────────────────────────────────────────┘
"""
import random  #For selecting random words
import os #Import functions for interacting with the operating system
import sys #Imports sys library for exiting the program

print("Welcome to Hangman!")  #Welcome message for the player

#List of hangman stages to show the progression of incorrect guesses
hangman_pics = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

def get_words_from_file(file_path):
    """
    Reads a list of words from a text file.

    Parameters:
    file_path (str): Path to the text file containing words.

    Returns:
    list: A list of words read from the file.
    """
    if not os.path.exists(file_path):  #Checks if the file exists
        print(f"File '{file_path}' not found. We will use a backup word bank instead")  #Error message if file not found
        return ["python", "keyboard", "computer", "science", "letters"]  #Returns default word list

    with open(file_path, "r") as file:  #Opens file in read mode
        words = file.read().splitlines()  #Reads all lines as a list
    return words  #Returns the list of words

def display_hidden(secret):
    """
    Create and return a hidden version of the word to be guessed.

    Parameters:
    secret (str): The secret word to be guessed by the player.

    Returns:
    list: A list containing the hidden word with underscores representing characters.
    """
    hidden = []  #Initialize empty list for hidden word
    for character in secret:  #Loops through each character in the secret word
        if character == " ":  #Checks if the character is a space
            hidden.append("  ")  #Appends double space for spaces
        else:  #For all other characters
            hidden.append("_ ")  #Appends an underscore with a space
    return hidden  #Returns the list of hidden characters


def play_game(words):
    """
    Single round of the Hangman game, allows the player to guess letters.

    Parameters:
    words (list): A list of words to select a secret word from.

    Returns:
    str: A string representing the outcome of the game ('win' or 'loss').
    """
    secret = random.choice(words)  #Chooses a random word from the list
    secret_list = list(secret)  #Converts the secret word to a list of characters
    hidden = display_hidden(secret)  #Creates hidden version of the word
    guesses = 0  #Initializes the number of incorrect guesses
    guessed_letters = []  #Initializes a list to track guessed letters

    print(hangman_pics[guesses])  #Shows the hangman stage
    print("".join(hidden))  #Displays the hidden word

    while "_ " in hidden and guesses < len(hangman_pics) - 1:  #Loops while there are hidden letters and lives remaining
        guess = input("\nEnter a letter: ").lower()  #Prompts the player for a guess

        if len(guess) != 1 or guess not in "abcdefghijklmnopqrstuvwxyz":  #Validates that input is a single letter
            print("Please enter a single letter.")  #Error message for invalid input
            continue  #Restarts the loop

        if guess in guessed_letters:  #Checks if the letter has already been guessed
            print("You already guessed that letter!")  #Warning for repeated guess
            continue  #Restarts the loop

        guessed_letters.append(guess)  #Adds the guessed letter to the list

        if guess in secret_list:  #Checks if the guessed letter is in the secret word
            for index in range(len(secret_list)):  #Loops through the secret word
                if guess == secret_list[index]:  #Matches guessed letter with positions
                    hidden[index] = guess  #Reveals the correct guess in the hidden word
            print("Correct!")  #Displays success message
        else:  #If the guessed letter is not in the word
            guesses += 1  #Increases the number of incorrect guesses
            print("Incorrect! You lost a life.")  #Displays failure message

        print("\n[Guessed letters:", ", ".join(guessed_letters), "]")  #Shows guessed letters
        print(hangman_pics[guesses])  #Shows the hangman stage
        print("".join(hidden))  #Displays the current state of the hidden word

    if "_ " in hidden:  #Checks if there are unrevealed letters remaining
        print("\nYou lose! The word was:", secret)  #Displays loss message with the correct word
        return "loss"  #Returns "loss" as the outcome
    else:  #If all letters are revealed
        print("\nCongratulations, you win!")  #Displays win message
        return "win"  #Returns "win" as the outcome


def main():
    """
    The main function to manage the game, tracking wins and losses,
    and offering replay options.
    """
    wins = 0  #Tracks the number of wins
    losses = 0  #Tracks the number of losses
    file_path = "words.txt"  #File path for the word list
    words = get_words_from_file(file_path)  #Reads words from the file

    while True:  #Game loop to play and count score
        result = play_game(words)  #Plays a single round
        if result == "win":  #Checks if the result is a win
            wins += 1  #Increases win count
        else:  #If the result is a loss
            losses += 1  #Increases loss count

        print(f"\nScore: {wins} Wins, {losses} Losses")  #Displays the current score

        while True: #Game loop to replay or exit
            play_again = input("Do you want to play again? (yes/no): ").lower() #Asks the player if they want to continue
            if play_again == "no": #Checks if user does not want to play again
                print("Thanks for playing! Goodbye.")  #Goodbye message
                sys.exit() #Exits the program
            elif play_again == "yes": #Checks if user wants to play again
                print("Okay!")
                break #Exits the loop
            else: #Checks if the player does not enter yes or no
                print("Please enter yes or no")  #Prompts user to enter yes or no
                continue #Restarts the loop

main() #Starts the game
