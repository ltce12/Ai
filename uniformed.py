from collections import deque

# BFS function
def bfs(graph, start, goal):
    # Queue for BFS that stores (node, path_to_node)
    queue = deque([(start, [start])])
    
    # Set to track visited nodes
    visited = set()

    while queue:
        # Dequeue a node
        (current_node, path) = queue.popleft()

        # If the current node is the goal, return the path
        if current_node == goal:
            return path
        
        # If the node has not been visited
        if current_node not in visited:
            visited.add(current_node)

            # Enqueue all adjacent nodes (neighbors) with their respective paths
            for neighbor in graph[current_node]:
                queue.append((neighbor, path + [neighbor]))
    
    return None  # Return None if no path is found

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
goal_node = 'F'

# Call BFS
path = bfs(graph, start_node, goal_node)

if path:
    print(f"Path found: {' -> '.join(path)}")
else:
    print("No path found")
