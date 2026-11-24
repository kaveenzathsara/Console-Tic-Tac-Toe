import random

board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

def reset_board():
    global board
    board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

def printboard():
    for i in board:
        for r in i:
            print(r + "  ", end="|  ")
        print()
        print("----------------")

def wincheck():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

def is_draw():
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ["X", "O"]:
                return False
    return True

def minimax(is_maximizing):
    winner = wincheck()
    if winner == "O":
        return 10
    if winner == "X":
        return -10
    if is_draw():
        return 0

    if is_maximizing:  # PC ("O") ge wara
        best_score = -100
        for i in range(3):
            for j in range(3):
                if board[i][j] not in ["X", "O"]:
                    temp = board[i][j]
                    board[i][j] = "O"
                    score = minimax(False)
                    board[i][j] = temp
                    best_score = max(score, best_score)
        return best_score

    else:  # Oyage ("X") wara
        best_score = 100
        for i in range(3):
            for j in range(3):
                if board[i][j] not in ["X", "O"]:
                    temp = board[i][j]
                    board[i][j] = "X"
                    score = minimax(True)
                    board[i][j] = temp
                    best_score = min(score, best_score)
        return best_score

def random_move():
    pc = random.randint(1, 9)
    row = (pc - 1) // 3
    col = (pc - 1) % 3
    while board[row][col] == "X" or board[row][col] == "O":
        pc = random.randint(1, 9)
        row = (pc - 1) // 3
        col = (pc - 1) % 3
    board[row][col] = "O"

def best_move():
    best_score = -100
    move = (0, 0)
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ["X", "O"]:
                temp = board[i][j]
                board[i][j] = "O"
                score = minimax(False)
                board[i][j] = temp
                if score > best_score:
                    best_score = score
                    move = (i, j)
    board[move[0]][move[1]] = "O"

def pc_move(difficulty):
    if difficulty == "1":  # Easy
        random_move()
    elif difficulty == "2":  # Medium (50% Smart, 50% Random)
        if random.choice([True, False]):
            best_move()
        else:
            random_move()
    else:  # Hard (Impossible)
        best_move()

def choose_difficulty():
    while True:
        choice = input("Select Difficulty (1 - Easy, 2 - Medium, 3 - Hard): ")
        if choice in ["1", "2", "3"]:
            return choice
        print("Invalid choice. Please enter 1, 2, or 3.")


print("Welcome to Tic Tac Toe Game")
difficulty = choose_difficulty()
printboard()
print("Start with player X")

while True:
    try:
        position = int(input("Enter where you want to place your mark (1-9) : "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 9.")
        continue

    if position < 1 or position > 9:
        print("Invalid input. Please enter a number between 1 and 9.")
        continue

    row = (position - 1) // 3
    col = (position - 1) % 3

    if board[row][col] == "X" or board[row][col] == "O":
        print("This position is already filled. Please choose another position.")
        continue

    board[row][col] = "X"

    if wincheck() == "X":
        printboard()
        print("You Win!")
        if input("Do you want to play again? (y/n): ").lower() == "y":
            reset_board()
            difficulty = choose_difficulty()
            printboard()
            continue
        break

    elif is_draw():
        printboard()
        print("Draw!")
        if input("Do you want to play again? (y/n): ").lower() == "y":
            reset_board()
            difficulty = choose_difficulty()
            printboard()
            continue
        break

    pc_move(difficulty)
    printboard()

    if wincheck() == "O":
        print("PC Wins!")
        if input("Do you want to play again? (y/n): ").lower() == "y":
            reset_board()
            difficulty = choose_difficulty()
            printboard()
            continue
        break