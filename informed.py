import heapq

# A utility function to print the 3x3 puzzle matrix
def print_puzzle(puzzle):
    for row in puzzle:
        print(" ".join(str(x) if x != 0 else '_' for x in row))
    print()

# Function to compute the Manhattan distance heuristic
def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:  # Skip the blank tile
                # Find the goal position of the current tile
                goal_x, goal_y = divmod(goal.index(state[i][j]), 3)
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

# Function to generate possible next states from the current state
def get_neighbors(state):
    # Find the position of the blank space (0)
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                blank_pos = (i, j)
                break

    # Define possible moves (up, down, left, right)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    
    for move in moves:
        new_x = blank_pos[0] + move[0]
        new_y = blank_pos[1] + move[1]
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            # Swap the blank with the adjacent tile
            new_state = [row[:] for row in state]  # Deep copy of the state
            new_state[blank_pos[0]][blank_pos[1]], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[blank_pos[0]][blank_pos[1]]
            neighbors.append(new_state)
    
    return neighbors

# A* Search algorithm
def a_star(start, goal):
    # Flatten the goal state for easier comparison and manhattan calculation
    goal_flat = [tile for row in goal for tile in row]

    # Priority queue for A*, using a heap (min-heap by default in Python)
    heap = []
    heapq.heappush(heap, (0, start, [], 0))  # (f(n), current state, path, g(n))
    
    visited = set()  # To store visited states
    
    while heap:
        # Pop the state with the lowest f(n) = g(n) + h(n)
        f, current_state, path, g = heapq.heappop(heap)
        
        # If the current state is the goal, return the path
        if current_state == goal:
            return path + [current_state]

        # Convert the current state to a tuple for hashing (immutable type)
        state_tuple = tuple(tuple(row) for row in current_state)
        
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        
        # Explore neighbors
        for neighbor in get_neighbors(current_state):
            # Calculate g(n) for the neighbor (cost from start)
            new_g = g + 1
            # Calculate h(n) using the Manhattan distance heuristic
            h = manhattan_distance(neighbor, goal_flat)
            # f(n) = g(n) + h(n)
            f = new_g + h
            heapq.heappush(heap, (f, neighbor, path + [current_state], new_g))
    
    return None  # If no solution is found

# Example initial state (0 represents the blank tile)
initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

# Goal state
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Running the A* algorithm
solution_path = a_star(initial_state, goal_state)

if solution_path:
    print("Solution found:")
    for state in solution_path:
        print_puzzle(state)
else:
    print("No solution found.")
