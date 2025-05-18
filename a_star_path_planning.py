import numpy as np
from queue import PriorityQueue

# Grid and obstacle setup
GRID_SIZE = 10
START = (0, 0)
GOAL = (8, 8)

# Randomly place obstacles
np.random.seed(1)
grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
obstacle_count = 15
for _ in range(obstacle_count):
    x, y = np.random.randint(0, GRID_SIZE, size=2)
    if (x, y) not in [START, GOAL]:
        grid[y][x] = 1

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(pos):
    neighbors = []
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = pos[0] + dx, pos[1] + dy
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and grid[ny][nx] == 0:
            neighbors.append((nx, ny))
    return neighbors

def a_star(start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    cost = {start: 0}

    while not frontier.empty():
        _, current = frontier.get()

        if current == goal:
            break

        for neighbor in get_neighbors(current):
            new_cost = cost[current] + 1
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + heuristic(goal, neighbor)
                frontier.put((priority, neighbor))
                came_from[neighbor] = current

    # Reconstruct path
    path = []
    node = goal
    while node:
        path.append(node)
        node = came_from.get(node)
    path.reverse()
    return path if path[0] == start else []

# Run A* and print results
path = a_star(START, GOAL)
print("Grid (1 = obstacle):")
print(grid)
print("\nPlanned Path from", START, "to", GOAL, ":")
print(path if path else "No path found.")
