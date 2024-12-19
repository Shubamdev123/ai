from collections import deque

def bfs(start, goal):
    queue = deque([(start, [])])
    visited = {tuple(start)}
    
    while queue:
        board, path = queue.popleft()
        if board == goal:
            return path + [board]

        zero = board.index(0)
        moves = []
        if zero >= 3: moves.append(zero - 3)  # Up
        if zero < 6: moves.append(zero + 3)   # Down
        if zero % 3 > 0: moves.append(zero - 1)  # Left
        if zero % 3 < 2: moves.append(zero + 1)  # Right

        for i in moves:
            new_board = board[:]
            new_board[zero], new_board[i] = new_board[i], new_board[zero]
            if tuple(new_board) not in visited:
                visited.add(tuple(new_board))
                queue.append((new_board, path + [board]))

    return None

# Example usage
start = [1, 2, 3, 4, 5, 6, 7, 8, 0]
goal = [1, 2, 3, 4, 5, 6, 7, 0, 8]
# goal = [1, 2, 0, 4, 5, 6, 7, 3, 8]

solution = bfs(start, goal)

if solution:
    for step in solution:
        print(step[:3])
        print(step[3:6])
        print(step[6:])
        print()
else:
    print("No solution found.")
