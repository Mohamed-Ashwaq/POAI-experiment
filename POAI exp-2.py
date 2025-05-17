# Mohamed ashwaq
# 241501113
# mohamedashwaq.y.2024.aiml@rajalakshmi.edu.in
def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Define the graph as an adjacency list
graph = {
    0: [1, 3],
    1: [4, 2],
    2: [],
    3: [5],
    4: [],
    5: []
}

visited = []
dfs(graph, 0, visited)

# Print DFS traversal order
print("".join(map(str, visited)))
