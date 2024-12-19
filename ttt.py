import random

def get_random_cell(mat):
    return random.randint(0, 2), random.randint(0, 2)

def assign_value(mat, row, col, value):
    mat[row][col] = value
    for row in mat:
        print(row)

def check_win(mat, value):
    for i in range(3):
        if all(mat[i][j] == value for j in range(3)) or all(mat[j][i] == value for j in range(3)):
            return True
    return all(mat[i][i] == value for i in range(3)) or all(mat[i][2 - i] == value for i in range(3))

def start_game():
    matrix = [[-1] * 3 for _ in range(3)]  # Initialize 3x3 matrix
    symbols = ['X', 'O']
    user = 0  # User 0 starts with 'X'

    for turns in range(9):
        print(f"\nUser {user + 1}'s turn")
        row, col = get_random_cell(matrix)
        
        while matrix[row][col] != -1:
            row, col = get_random_cell(matrix)
        
        assign_value(matrix, row, col, symbols[user])
        
        if check_win(matrix, symbols[user]):
            print(f"User {user + 1} ({symbols[user]}) wins!")
            return
        
        user = 1 - user  # Switch player

    print("It's a draw!")

start_game()
