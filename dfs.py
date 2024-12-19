def dfs(graph, start):
    visited = []           # List to keep track of visited nodes
    stack = [start]        # Use a stack initialized with the start node
    
    while stack:
        node = stack.pop()  # Take the last node from the stack
        if node not in visited:
            visited.append(node)  # Mark the node as visited
            stack.extend(reversed(graph[node]))  # Add unvisited neighbors to the stack
    
    return visited

# Example usage
graph = {
    0: [1],
    1: [2, 3],
    2: [0, 4],
    3: [4],
    4: []
}
print("DFS starting from vertex 0:", dfs(graph, 0))
