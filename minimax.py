import math

def minimax(depth, node_index, is_max, scores, max_depth):
    if depth == max_depth:  # Base case: Return leaf node value
        return scores[node_index]

    if is_max:  # Maximizer's turn
        return max(
            minimax(depth + 1, node_index * 2, False, scores, max_depth),
            minimax(depth + 1, node_index * 2 + 1, False, scores, max_depth)
        )
    else:  # Minimizer's turn
        return min(
            minimax(depth + 1, node_index * 2, True, scores, max_depth),
            minimax(depth + 1, node_index * 2 + 1, True, scores, max_depth)
        )

# Example usage
scores = [3, 5, 2, 9, 12, 5, 23, 23]  # Leaf node values of the tree
max_depth = int(math.log2(len(scores)))  # Depth of the binary tree

# Find the optimal value using Minimax
optimal_value = minimax(0, 0, True, scores, max_depth)
print("The optimal value is:", optimal_value)
