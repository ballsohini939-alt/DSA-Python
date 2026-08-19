graph = {}

# Add vertices
graph["A"] = []
graph["B"] = []
graph["C"] = []
graph["D"] = []


# Add edges
graph["A"].append("B")
graph["A"].append("C")

graph["B"].append("A")
graph["B"].append("D")

graph["C"].append("A")
graph["C"].append("D")

graph["D"].append("B")
graph["D"].append("C")


# Display graph
for vertex in graph:
    print(vertex, "->", graph[vertex])