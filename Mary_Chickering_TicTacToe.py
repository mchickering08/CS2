""""
┌───────────────────────────────────────────────────────────────────────────┐
│                               Tic Tac Toe                                 │
├───────────────────────────────────────────────────────────────────────────┤
│ Name: Mary Chickering                                                     │
│ Log: Finished project (1.0)                                               |
| Bugs: N/K                                                                 │
│ Description: User can choose to play either one or two player TTT. If user|
| chooses one player TTT, they play against the bot. If user chooses two    |
| player TTT, they play against a human (both on same computer)             |                             
└───────────────────────────────────────────────────────────────────────────┘
"""
import random  #Imports random library for bot decision-making
import sys #Imports sys library for exiting the program
def create_board(box):
    """
     Prints the current state of the Tic Tac Toe board in a 3x3 format

    Args:
        Args: box (list): The 3x3 Tic Tac Toe board

    Returns:
        None
    """
    for i in range(len(box)): #Iterate through each row in the board
        for j in range(len(box[i])): #Iterate through each cell in the row
            print(box[i][j], end=' ') # Print cell value with a space
        print() #Prints the moving to the next line after each row
def get_move(box, user_or_bot, XO): 
    """
    Handles a player's or bot's move and updates the board

    Args:
        box (list): The current Tic Tac Toe board
        user_or_bot (str): Specifies whether the move is by the "user" or "bot"
        XO (str): The symbol ('X' or 'O') to place on the board

    Returns:
        None
    """
    if end_game(box) == True: #If the end_game function returns as true
        print("Board is full. Try again.") #Print that the board is full
        main() #Run the main
    while True:
        if user_or_bot == "user": #If it is user's turn
            move = input("Enter spot 1 - 9: ") #Prompts user for a move
        else:
            move = random.choice(list("123456789"))  #Bot randomly selects a spot
        #Places the user/bot input to board positions, checks if the spot is available and updates board
        if move == "1" and box[0][0] == 1:
            box[0][0] = XO
        elif move == "2" and box[0][1] == 2:
            box[0][1] = XO
        elif move == "3" and box[0][2] == 3:
            box[0][2] = XO
        elif move == "4" and box[1][0] == 4:
            box[1][0] = XO
        elif move == "5" and box[1][1] == 5:
            box[1][1] = XO
        elif move == "6" and box[1][2] == 6:
            box[1][2] = XO
        elif move == "7" and box[2][0] == 7:
            box[2][0] = XO
        elif move == "8" and box[2][1] == 8:
            box[2][1] = XO
        elif move == "9" and box[2][2] == 9:
            box[2][2] = XO
        else: #If the user's spot is not available or not open
            if user_or_bot == "user": 
                print("Please enter an available spot") 
            continue
        create_board(box) #Prints the updated board
        break
def choose_starting_player(box, player1_XO, player2_XO, user_or_bot):
    """
    Determines which player or bot starts and alternates turns

    Args:
        box (list): The current Tic Tac Toe board
        player1_XO (str): Player 1's symbol ('X' or 'O')
        player2_XO (str): Player 2's or bot's symbol ('X' or 'O')
        user_or_bot (str): Indicates if player 2 is a "user" or "bot"

    Returns:
        None
    """
    while True:
        #Assigns user or bot to the player variables
        if user_or_bot == "user":
            player1 = "Player 1's"
            player2 = "Player 2's"
        else:
            player1 = "User's"
            player2 = "Bot's"
        turn = random.choice(["p1", "p2"]) #Randomly choose starting player
        for count in range(9):  #Maximum of 9 moves on a 3x3 board
            if turn == "p1":
                print(player1, "turn") #Prints player 2's turn
                get_move(box, "user", player1_XO) #Runs the get move function
                if winner(box, player1_XO) == False: #If winner function returns false for player 1
                    break 
                turn = "p2" #Moves to player 2's turn
                count += 1 #Adds one to the count
            else:
                print(player2, "turn") #Print  player 1's turn
                get_move(box, user_or_bot, player2_XO) #Runs the get move function 
                if winner(box, player2_XO) == False: #If winner function returns false for player 2
                    break
                turn = "p1" #Moves to player 1's turn
                count += 1 #Adds one to the count
def play_again(XO):
    """
    Prompts the user to play again after a win

    Args:
        XO (str): The winning symbol ('X' or 'O')

    Returns:
        None
    """
    winner = False #Sets winner to false
    print("Player", XO, "won!") #Prints the winner
    go_again = input("Would you like to play again? (yes or no)") #Asks if user wants to play again
    if go_again == "yes":
        main() #If player says yes, goes back to main
    elif go_again == "no":
        print("Okay bye.")
        sys.exit() #If player says no, exits the program
    return winner
def winner(box, XO):
    """
    Checks if the given player (XO) has won the game.

    Args:
        box (list): The current Tic Tac Toe board.
        XO (str): The player's symbol ('X' or 'O').

    Returns:
        bool: True if no winner yet, False if a winner is found.
    """
    winner = True #Sets winner to true
    for row in range (0, 3): #Check rows
        if box[row][0] == box[row][1] == box[row][2] == XO: #If there are three in a row in a row
            play_again(XO) #Asks player if they want to play again through the play_again function
    for col in range (0, 3): #Checks columns
        if box[0][col] == box[1][col] == box[2][col] == XO: #If there are three in a row in a column
            play_again(XO) #Asks player if they want to play again through the play_again function
    if box[0][0] == box[1][1] == box[2][2] == XO or box[0][2] == box[1][1] == box[2][0] == XO: #Checks diagonals
        play_again(XO) #Asks player if they want to play again through the play_again function
    return winner #Returns winner as True as defined before
def choose_player():
    """
    Prompts the user to choose their symbol ('X' or 'O')

    Returns:
        tuple: Player 1's and Player 2's symbols.
    """
    while True:
        player1 = input("Player one: 'X' or 'O'? ").lower() #Propts the user if they want to be 'X' or 'O' 
        if player1 == "x": #If user enter X
            return "X", "O" #Return p1 as X and p2 as O
        elif player1 == "o": #If user enters O
            return "O", "X" #Returns p1 as O and p2 as X
        else:
            print("Invalid input. Please enter 'X' or 'O'.") #If user doesn't enter X or O, prints invalid
def end_game(box):
    """
    Checks if the game board is full.

    Args:
        box (list): The current Tic Tac Toe board.

    Returns:
        bool: True if the board is full, False otherwise.
    """
    if (1 and 2 and 3) not in box[0] and (4 and 5 and 6) not in box[1] and (7 and 8 and 9) not in box[2]: #If all numbers are not in the box (if board is full)
        return True 
    else:
        return False

play_game = input("Do you want to play Tic Tac Toe? (yes or no)") #Asks user if they want to play (outside the main so it does not repeat opening question when player plays again)
def main():
    """
    Main function to start and play the game
    """
    while True:
        if play_game.lower() == "yes": #If user says yes
            box = [ #Creates the Tic Tac Toe board as a 3x3 list
                    [1,2,3],
                    [4,5,6],
                    [7,8,9]
                ]
            print("YAY")
            break
        elif play_game.lower() == "no": #If the user says no
            print("Say yes. Try again") #Tell them to try again and circle back to the top of loop
            continue
        else: #IF user does not say yes or no
            print("I literally gave you the options to choose from. TRY AGAIN") #Tell them to try again and circle back to the top of loop
            continue
    while True:
        player_amount = input("One or two players?") #Ask user if they want one or two player game mode
        if player_amount.lower() != "one" and player_amount.lower() != "two" and player_amount.lower() != "1" and player_amount.lower() != "2": #IF player does not equal one or two
            print("Please enter one or two") #Ask them to enter an input in between those two and go to top of loop
            continue
        print("You've selected", player_amount, "players") #Prints their selected game mode
        player1_XO, player2_XO = choose_player() #USes choose_player function to see who goes first (random)
        print("This is the tic tac toe board. Please enter one of the following numbers to mark where you want to go")
        create_board(box) #Prints the blank starting board
        if player_amount.lower() == "one": #If the player chooses "one" for the game mode/amt of players
            choose_starting_player(box, player1_XO, player2_XO, "bot") #Runs choose_starting_player function for bot vs. player
            break
        elif player_amount.lower() == "two": #If the player chooses "two" for the game mode/amt of players
            choose_starting_player(box, player1_XO, player2_XO, "user") #Runs choose_starting_player function for player vs. player
            break
main() #Runs the main