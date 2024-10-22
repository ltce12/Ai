import random

# Function to calculate the number of queens attacking each other
def calculate_attacks(state):
    attacks = 0
    n = len(state)
    
    for i in range(n):
        for j in range(i + 1, n):
            # Check if queens are on the same row or on the same diagonal
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
                
    return attacks

# Function to generate neighbors by moving each queen within its column
def get_neighbors(state):
    neighbors = []
    n = len(state)
    
    for col in range(n):
        for row in range(n):
            if state[col] != row:  # Avoid placing the queen in the same row
                new_state = list(state)
                new_state[col] = row
                neighbors.append(new_state)
                
    return neighbors

# Hill Climbing algorithm
def hill_climbing(n=8):
    # Start with a random initial state: one queen in each column, random row
    current_state = [random.randint(0, n - 1) for _ in range(n)]
    current_attacks = calculate_attacks(current_state)
    
    while True:
        neighbors = get_neighbors(current_state)
        
        # Find the best neighbor (least number of attacks)
        best_neighbor = None
        best_attacks = current_attacks
        
        for neighbor in neighbors:
            attacks = calculate_attacks(neighbor)
            if attacks < best_attacks:
                best_attacks = attacks
                best_neighbor = neighbor
        
        # If no better neighbor is found, return the current state (local optimum)
        if best_attacks >= current_attacks:
            break
        
        # Move to the better neighbor
        current_state = best_neighbor
        current_attacks = best_attacks
    
    return current_state, current_attacks

# Example usage: Solve the 8-Queens problem
solution, attacks = hill_climbing(n=8)

print("Solution:", solution)
print("Number of attacking pairs:", attacks)
