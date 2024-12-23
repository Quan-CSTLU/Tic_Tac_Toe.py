import math
X = "X"
O = "O"
EMPTY = None
def board_status():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# Check winner
def winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None

# Kiểm tra trạng thái game đã kết thúc chưa
def terminal(board):
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True

# hàm điểm thưởng nếu X wi thì max=1, O win min = -1, draw thì =0
def utility(board):
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

#minimax + anpal beta
def minimax(board, is_maximizing, alpha, beta):
    if terminal(board):
        return utility(board)
    
    if is_maximizing:
        max_eval = -1
        for row in range(3):
            for col in range(3):
                if board[row][col] is EMPTY:
                    board[row][col] = X
                    eval = minimax(board, False, alpha, beta)
                    board[row][col] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = 1
        for row in range(3):
            for col in range(3):
                if board[row][col] is EMPTY:
                    board[row][col] = O
                    eval = minimax(board, True, alpha, beta)
                    board[row][col] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

#Tìm nước đi tốt nhất
def best_move(board):
    best_val = -1
    move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] is EMPTY:
                board[row][col] = X
                move_val = minimax(board, False, -1, 1)
                board[row][col] = EMPTY
                if move_val > best_val:
                    best_val = move_val
                    move = (row, col)
    return move

#main
board = board_status()
print("Board status:")
for row in board:
    print(row)
move = best_move(board)
print(f"Best move for X: {move}")
