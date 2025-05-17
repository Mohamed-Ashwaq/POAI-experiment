import heapq

# Manhattan distance heuristic function
def heuristic(state, goal):
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

# Function to get valid neighbors (up, down, left, right)
def get_neighbors(state):
    x, y = state
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

# A* Search Algorithm
def a_star_search(start, goal):
    open_list = [(0, start)]  # Priority queue (cost, state)
    came_from = {start: None}  # Track the path
    g_score = {start: 0}  # Cost from start to current node

    while open_list:
        _, current = heapq.heappop(open_list)  # Get node with lowest cost

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]  # Reverse the path from start to goal

        for neighbor in get_neighbors(current):
            if neighbor not in g_score or g_score[current] + 1 < g_score[neighbor]:
                g_score[neighbor] = g_score[current] + 1
                f_score = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))
                came_from[neighbor] = current  # Track movement

    return None  # No path found

# Example usage
start = (0, 0)
goal = (3, 3)
path = a_star_search(start, goal)

print("Path from start to goal:", path)
