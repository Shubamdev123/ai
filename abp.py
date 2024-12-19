import math

def alpha_beta(depth, index, is_max, scores, max_depth, alpha=float('-inf'), beta=float('inf')):
    if depth == max_depth:  # Base case: if at the target depth, return the leaf node score
        return scores[index]

    if is_max:  # Maximizer's turn
        best = float('-inf')  # Initialize best value as -infinity
        for i in range(2):  # Two children (binary tree)
            value = alpha_beta(depth + 1, index * 2 + i, False, scores, max_depth, alpha, beta)
            best = max(best, value)  # Update the best value
            alpha = max(alpha, value)  # Update alpha
            if beta <= alpha:  # Prune if alpha is greater than or equal to beta
                break
        return best
    else:  # Minimizer's turn
        best = float('inf')  # Initialize best value as +infinity
        for i in range(2):  # Two children (binary tree)
            value = alpha_beta(depth + 1, index * 2 + i, True, scores, max_depth, alpha, beta)
            best = min(best, value)  # Update the best value
            beta = min(beta, value)  # Update beta
            if beta <= alpha:  # Prune if alpha is greater than or equal to beta
                break
        return best

# Example usage
scores = [3, 5, 2, 9, 12, 5, 23, 23]  # Leaf nodes of the tree
max_depth = int(math.log2(len(scores)))  # Depth of the tree

optimal_value = alpha_beta(0, 0, True, scores, max_depth)  # Call the alpha-beta pruning function
print("The optimal value is:", optimal_value)
