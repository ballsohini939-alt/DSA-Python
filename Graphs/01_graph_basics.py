# Create a graph using a dictionary
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

# Display the graph
for vertex in graph:
    print(vertex, "->", graph[vertex])