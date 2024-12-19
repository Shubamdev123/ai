def a_star(graph, heuristic, cost, start, goal):
    open_list = [start]  # Nodes to explore
    visited = set()  # Nodes already explored
    parent = {start: None}  # To track the path
    path_cost = {start: 0}  # Actual cost from the start to each node

    while open_list:
        # Find the node with the lowest f(n) = g(n) + h(n)
        current = min(open_list, key=lambda node: path_cost[node] + heuristic[node])
        open_list.remove(current)  # Remove the current node from open list

        if current == goal:  # If goal is reached, reconstruct the path and total cost
            path = []
            total_cost = path_cost[goal]
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1], total_cost  # Return reversed path and cost

        visited.add(current)  # Mark the current node as visited

        for neighbor in graph.get(current, []):  # Explore neighbors
            new_cost = path_cost[current] + cost[neighbor]  # Calculate new cost
            if neighbor not in visited or new_cost < path_cost.get(neighbor, float('inf')):
                path_cost[neighbor] = new_cost  # Update the cost for the neighbor
                parent[neighbor] = current  # Update the parent of the neighbor
                if neighbor not in open_list:
                    open_list.append(neighbor)  # Add the neighbor to the open list

    return None, float('inf')  # Return None if no path is found


# Example input
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5, 6],
    5: [8],
    6: [9],
    4: [7]
}

heuristic = [13, 12, 4, 7, 3, 8, 2, 0, 4, 9]  # Estimated cost to goal
cost = [0, 3, 2, 4, 1, 3, 10, 3, 5, 2]  # Actual cost from the start
start = 0
goal = 7

# Run A* search
path, total_cost = a_star(graph, heuristic, cost, start, goal)
if path:
    print("Path:", path)
    print("Total Cost:", total_cost)
else:
    print("No path found.")
