def bfs(graph, start):
    visited = []           # List to keep track of visited nodes
    queue = [start]        # Use a queue initialized with the start node
    
    while queue:
        node = queue.pop(0)  # Take the first node from the queue
        if node not in visited:
            visited.append(node)  # Mark the node as visited
            queue.extend(graph[node])  # Add unvisited neighbors to the queue
    
    return visited

# Example usage
graph = {
    0: [1],
    1: [2, 3],
    2: [0, 4],
    3: [4],
    4: []
}
print("BFS starting from vertex 0:", bfs(graph, 0))
