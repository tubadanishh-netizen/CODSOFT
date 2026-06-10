# The board has 9 positions, all empty at start
# It looks like this:
# 1 | 2 | 3
# 4 | 5 | 6
# 7 | 8 | 9
board = [" " for i in range(9)]

# This function draws the board on screen
def print_board():
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

# This function checks if a player has won
# player will be either "X" or "O"
def check_winner(player):
    # All 8 ways to win in tic tac toe
    # 3 rows + 3 columns + 2 diagonals
    winning_combinations = [
        [0,1,2],  # top row
        [3,4,5],  # middle row
        [6,7,8],  # bottom row
        [0,3,6],  # left column
        [1,4,7],  # middle column
        [2,5,8],  # right column
        [0,4,8],  # diagonal top-left to bottom-right
        [2,4,6]   # diagonal top-right to bottom-left
    ]
    # Check each winning combination
    for combo in winning_combinations:
        # If all 3 positions in a combo belong to same player
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True  # This player won!
    return False  # Nobody won yet

# This function checks if all 9 squares are filled
def is_board_full():
    # If no empty space exists, board is full
    return " " not in board

# This is the BRAIN of the AI — Minimax algorithm
# It tries every possible move and picks the best one
# is_ai_turn = True means AI is deciding, False means simulating player
def minimax(is_ai_turn):
    # First check if game is already over
    # If AI (O) won, return 1 (good for AI)
    if check_winner("O"):
        return 1
    # If player (X) won, return -1 (bad for AI)
    if check_winner("X"):
        return -1
    # If board is full with no winner, return 0 (draw)
    if is_board_full():
        return 0

    # AI's turn — AI wants to MAXIMIZE the score
    if is_ai_turn:
        best_score = -1000  # Start with very low score
        # Try every empty square
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"  # AI places O here temporarily
                # Simulate what happens next (now player's turn)
                score = minimax(False)
                board[i] = " "  # Undo the move
                # Keep track of highest score found
                if score > best_score:
                    best_score = score
        return best_score

    # Player's turn — Player wants to MINIMIZE the score
    else:
        best_score = 1000  # Start with very high score
        # Try every empty square
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"  # Player places X here temporarily
                # Simulate what happens next (now AI's turn)
                score = minimax(True)
                board[i] = " "  # Undo the move
                # Keep track of lowest score found
                if score < best_score:
                    best_score = score
        return best_score

# This function makes the AI pick its best move
def ai_move():
    best_score = -1000  # Start with very low score
    best_position = 0   # Will store the best position found

    # Try every empty square
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"  # Try placing O here
            # See how good this move is
            score = minimax(False)
            board[i] = " "  # Undo the move
            # If this move is better than previous best
            if score > best_score:
                best_score = score
                best_position = i  # Remember this position

    # Now actually place O at the best position found
    board[best_position] = "O"
    print(f"AI placed O at position {best_position + 1}")

# This is the main game function
def play_game():
    print("Welcome to Tic Tac Toe!")
    print("You are X, AI is O")
    print("Positions are numbered like this:")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")
    print()

    # Keep playing until game ends
    while True:
        # Show current board
        print_board()

        # YOUR TURN
        # Keep asking until valid move entered
        while True:
            try:
                # Get position from player (1-9)
                move = int(input("Your move (1-9): "))
                # Convert to index (1 becomes 0, 9 becomes 8)
                move = move - 1
                # Check if position is valid and empty
                if 0 <= move <= 8 and board[move] == " ":
                    break  # Valid move, exit this inner loop
                else:
                    print("Invalid move! Try again.")
            except:
                print("Please enter a number between 1-9!")

        # Place X at chosen position
        board[move] = "X"

        # Check if player won after their move
        if check_winner("X"):
            print_board()
            print("Congratulations! You won!")
            break

        # Check if board is full after player move
        if is_board_full():
            print_board()
            print("It's a draw!")
            break

        # AI'S TURN
        print("AI is thinking...")
        ai_move()

        # Check if AI won after its move
        if check_winner("O"):
            print_board()
            print("AI wins! Better luck next time!")
            break

        # Check if board is full after AI move
        if is_board_full():
            print_board()
            print("It's a draw!")
            break

# Start the game!
play_game()
