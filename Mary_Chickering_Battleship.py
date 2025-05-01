""""
┌───────────────────────────────────────────────────────────────────────────┐
│                               Battleship                                  │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: Mary Chickering                                                     │
│ Log: Finished project (1.0)                                               |
| Bugs: N/K                                                                 │
│ Description: Terminal-based version of the classic Battleship game,       |
| written in Python. It supports both Player vs Player and Player vs        |
| Computer modes, with selectable difficulty for the computer. The game     |
| includes sound effects for hits and misses a clean interface using emojis |
| Tester: Kaia Novack                                                       |
└───────────────────────────────────────────────────────────────────────────┘
"""
import random                                                                                                   #For generating random ship placements and computer guesses
import os                                                                                                       #To clear the terminal screen between turns
import winsound                                                                                                 #To play .wav sound effects for hits and misses (Windows only)

def initialize_board():
    """
    Purpose: Create a new empty 5x5 game board.
    Returns:
        A 5x5 list of lists filled with blank spaces.
    """
    return [[" " for _ in range(5)] for _ in range(5)]                                                          #Creates a 5x5 list of spaces

def display_board(game_board, hide_ships=False):
    """
    Purpose: Display the game board with emojis to indicate hits, misses, and water.
    Args:
        game_board: The board to display (list of lists).
        hide_ships: If True, ships are hidden by replacing 'S' with water.
    Output:
        None; prints the formatted board.
    """
    print("   0  1  2  3  4")                                                                                   #Print column headers
    for index, row in enumerate(game_board):                                                                    #Loop over each row with its index
        row_display = ""                                                                                        #Initialize an empty string to build this row
        for cell in row:                                                                                        #Loop through each cell in the row
            if cell == "X":                                                                                     #If it's a hit
                row_display += "💥 "                                                                            #Show explosion emoji
            elif cell == "O":                                                                                   #If it's a miss
                row_display += "❌ "                                                                            #Show red X emoji
            elif cell == "S":                                                                                   #If it's a ship
                row_display += "🌊 " if hide_ships else "🌊 "                                                   #Show water 
            else:
                row_display += "🌊 "                                                                            #If empty, show water
        print(str(index) + "  " + row_display)                                                                  #Print the row number and the built row string

def get_valid_coordinates(prompt_text):
    """
    Purpose: Prompt the user to enter valid board coordinates.
    Args:
        prompt_text: The prompt message for the user.
    Returns:
        A tuple (row, col) if valid input is given.
    """
    while True:                                                                                                 #Repeat until valid input
        user_input = input(prompt_text)                                                                         #Prompt user for input
        parts = user_input.strip().split()                                                                      #Split input by space
        if len(parts) != 2:                                                                                     #Ensure exactly two values
            print("Error: Enter exactly two numbers separated by a space.")                                     #Error message
            continue                                                                                            #Re-prompt
        try:
            row, col = int(parts[0]), int(parts[1])                                                             #Convert input to integers
            if 0 <= row <= 4 and 0 <= col <= 4:                                                                 #Ensure values are in range
                return row, col                                                                                 #Return as a tuple
            else:
                print("Error: Numbers must be between 0 and 4.")                                                #Out-of-range message
        except ValueError:                                                                                      #If input isn’t valid integers
            print("Error: Both entries must be numbers.")                                                       #Type error message

def manual_ship_placement(ship_board, player_name):
    """
    Purpose: Allow a player to manually place four ships.
    Args:
        ship_board: The board to place ships on.
        player_name: Name of the player placing ships.
    """
    ships_added = 0                                                                                             #Start with 0 ships
    print(player_name + ", place your 4 ships:")                                                                #Prompt player to place ships
    while ships_added < 4:                                                                                      #Until 4 ships placed
        row, col = get_valid_coordinates(f"Enter row and column (0-4) for ship {ships_added + 1}: ")            #Get input
        if ship_board[row][col] == " ":                                                                         #If the spot is empty
            ship_board[row][col] = "S"                                                                          #Place a ship
            ships_added += 1                                                                                    #Increment ship counter
        else:
            print("That spot is already occupied.")                                                             #Spot is taken

def auto_place_ships(ship_board):
    """
    Purpose: Automatically place four ships at random coordinates.
    Args:
        ship_board: The board to update with ships.
    """
    ships_added = 0                                                                                             #Initialize counter
    while ships_added < 4:                                                                                      #Loop until 4 ships placed
        row, col = random.randint(0, 4), random.randint(0, 4)                                                   #Pick random spot
        if ship_board[row][col] == " ":                                                                         #If spot is empty
            ship_board[row][col] = "S"                                                                          #Place ship
            ships_added += 1                                                                                    #Increment count

def process_turn(opponent_board, tracking_board, player_name, computer_mode=False, difficulty=1, last_hits=[]):
    """
    Purpose: Execute one turn for a player or the computer.
    Args:
        opponent_board: The opponent's ship board.
        tracking_board: The guessing player's tracking board.
        player_name: Name of the player taking the turn.
        computer_mode: If True, enables computer logic.
        difficulty: AI level (1 for random, 2 for smart).
        last_hits: Coordinates of prior hits (for smart AI).
    Returns:
        Updated last_hits list for AI targeting.
    """
    while True:                                                                                                 #Keep asking until a valid guess is made
        if computer_mode:                                                                                       #If it's the computer's turn
            if difficulty == 1 or not last_hits:                                                                #Easy mode or nothing to base smart guesses on
                guess_row, guess_col = random.randint(0, 4), random.randint(0, 4)                               #Random guess
            else:
                base_hit = random.choice(last_hits)                                                             #Pick a previous hit
                possible_guesses = [(base_hit[0] + dr, base_hit[1] + dc)
                                    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]
                                    if 0 <= base_hit[0] + dr <= 4 and 0 <= base_hit[1] + dc <= 4]               #Get neighbors
                random.shuffle(possible_guesses)                                                                #Randomize order
                for r, c in possible_guesses:
                    if tracking_board[r][c] == " ":                                                             #Only pick unguessed spot
                        guess_row, guess_col = r, c                                                             #Use it
                        break
                else:
                    guess_row, guess_col = random.randint(0, 4), random.randint(0, 4)                           #Backup random guess
            print(f"{player_name} guessed ({guess_row}, {guess_col})")                                          #Show guess
        else:
            guess_row, guess_col = get_valid_coordinates(f"{player_name}, guess row and column (0-4): ")        #Get user guess

        if tracking_board[guess_row][guess_col] == " ":                                                         #Check if spot hasn’t been guessed yet
            if opponent_board[guess_row][guess_col] == "S":                                                     #If it's a ship
                print("Hit!")                                                                                   #Announce hit
                tracking_board[guess_row][guess_col] = "X"                                                      #Mark hit on tracking board
                opponent_board[guess_row][guess_col] = "X"                                                      #Mark hit on opponent board
                winsound.PlaySound(r'C:\Users\mchickering27\Downloads\battleship\hit.wav', winsound.SND_ALIAS)  #Play sound
                if computer_mode and difficulty == 2:                                                           #If difficult mode
                    last_hits.append((guess_row, guess_col))                                                    #Save this hit
            else:
                print("Miss.")                                                                                  #Announce miss
                tracking_board[guess_row][guess_col] = "O"                                                      #Mark miss
                opponent_board[guess_row][guess_col] = "O"                                                      #Mark miss on opponent's board
                winsound.PlaySound(r'C:\Users\mchickering27\Downloads\battleship\miss.wav', winsound.SND_ALIAS) #Play sound
            break                                                                                               #End the turn
        else:
            if not computer_mode:
                print("You already guessed that spot.")                                                         #Already guessed
    return last_hits                                                                                            #Return updated memory for difficult mode

def main():
    """
    Purpose: Launch and control the overall flow of the Battleship game.
    """
    print("Welcome to Battleship!")                                                                             #Start message

    while True:
        print("Choose your mode:")                                                                              #Show options
        print("1 - Player vs Player")
        print("2 - Player vs Computer")
        mode_choice = input("Enter your choice (1 or 2): ").strip()                                             #Get user input
        if mode_choice in ["1", "2"]:                                                                           #Valid input check
            break
        else:
            print("Invalid input. Please enter 1 or 2.")                                                        #Invalid entry

    player1_board = initialize_board()                                                                          #Create player 1 board
    player1_tracking = initialize_board()                                                                       #Create tracking board for player 1
    player2_board = initialize_board()                                                                          #Create board for player 2 or computer
    player2_tracking = initialize_board()                                                                       #Create tracking board for player 2 or computer

    if mode_choice == "1":                                                                                      #PvP mode
        manual_ship_placement(player1_board, "Player 1")                                                        #Player 1 places ships
        os.system('cls' if os.name == 'nt' else 'clear')                                                        #Clear screen for fairness
        manual_ship_placement(player2_board, "Player 2")                                                        #Player 2 places ships
        difficulty_choice = 1                                                                                   #Placeholder
    else:
        manual_ship_placement(player1_board, "Player")                                                          #Player places ships
        auto_place_ships(player2_board)                                                                         #Computer places ships randomly
        while True:
            print("Choose computer difficulty:")                                                                #Ask for difficulty
            print("1 - Easy (random)")
            print("2 - Hard (smart targeting)")
            difficulty_input = input("Enter difficulty (1 or 2): ").strip()                                     #Get input
            if difficulty_input in ["1", "2"]:
                difficulty_choice = int(difficulty_input)                                                       #Save difficulty
                break
            else:
                print("Invalid input. Please enter 1 or 2.")                                                    #Retry

    player1_turns = 0                                                                                           #Initialize turns
    player2_turns = 0
    last_computer_hits = []                                                                                     #Diffuclty mode memory

    while player1_turns < 10 or player2_turns < 10:                                                             #Loop through game
        if player1_turns < 10:
            os.system('cls' if os.name == 'nt' else 'clear')                                                    #Clear screen
            print(f"\nPlayer 1's Turn! (Turn {player1_turns + 1} of 10)")                                       #Show turn
            print("\nYour guesses:")
            display_board(player1_tracking)                                                                     #Show guesses
            print("\nYour own board:")
            display_board(player1_board, hide_ships=(mode_choice == "1"))                                       #Show own board
            process_turn(player2_board, player1_tracking, "Player 1")                                           #Process guess
            player1_turns += 1                                                                                  #Increment turns
            if mode_choice == "1":
                input("\nHit enter to pass to Player 2...")                                                     #Pause
                os.system('cls' if os.name == 'nt' else 'clear')                                                #Clear

        if player2_turns < 10:
            if mode_choice == "1":
                print(f"\nPlayer 2's Turn! (Turn {player2_turns + 1} of 10)")                                   #Show turn
                print("\nYour guesses:") 
                display_board(player2_tracking)                                                                 #Show other player's board (as reference)
                print("\nYour own board:")
                display_board(player2_board, hide_ships=True)                                                   #Show own board
                process_turn(player1_board, player2_tracking, "Player 2")                                       #Play turn
                input("\nHit enter to pass to Player 1...")
                os.system('cls' if os.name == 'nt' else 'clear')                                                #Clear terminal to pass board
            else:
                print(f"\nComputer's Turn! (Turn {player2_turns + 1} of 10)")
                last_computer_hits = process_turn(player1_board, player2_tracking, "Computer", True, difficulty_choice, last_computer_hits) #Computer turn
            player2_turns += 1

    player1_hits = sum(row.count("X") for row in player1_tracking)                                              #Count Player 1 hits
    player2_hits = sum(row.count("X") for row in player2_tracking)                                              #Count Player 2/computer hits

    print("\nGame Over!")                                                                                       #End message
    print(f"Player 1 hits: {player1_hits}")                                                                     #Score
    print(f"{'Player 2' if mode_choice == '1' else 'Computer'} hits: {player2_hits}")

    if player1_hits > player2_hits:
        print("Player 1 wins!")                                                                                 #Declare winner
    elif player2_hits > player1_hits:
        print("Player 2 wins!" if mode_choice == "1" else "Computer wins!")
    else:
        print("It's a tie!")                                                                                    #Tie message

main()                                                                                                          #Run the game
