def water_jug_problem(jug1_capacity, jug2_capacity, target):
    jug1, jug2 = 0, 0  # Both jugs start empty
    steps = [(jug1, jug2)]  # Track steps for solution

    while jug1 != target and jug2 != target:
        if jug1 == 0:  # If Jug1 is empty, fill it
            jug1 = jug1_capacity
        elif jug2 == jug2_capacity:  # If Jug2 is full, empty it
            jug2 = 0
        else:  # Pour water from Jug1 into Jug2
            transfer = min(jug1, jug2_capacity - jug2)
            jug1 -= transfer
            jug2 += transfer
        
        steps.append((jug1, jug2))  # Record the state after each step

    return steps  # Return the sequence of steps

# Example Usage
jug1_capacity = int(input("Enter capacity of Jug1: "))  # Input Jug1 capacity
jug2_capacity = int(input("Enter capacity of Jug2: "))  # Input Jug2 capacity
target = int(input("Enter target amount: "))  # Input target amount

# Find and display the steps
steps = water_jug_problem(jug1_capacity, jug2_capacity, target)
for jug1, jug2 in steps:  # Print each step in a readable format
    print(f"Jug1: {jug1}, Jug2: {jug2}")
