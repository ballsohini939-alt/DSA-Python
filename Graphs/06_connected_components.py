# ==========================================
# CONNECTED COMPONENTS
# ==========================================


graph = {
    "A": ["B", "C"],
    "B": ["A"],
    "C": ["A"],
    "D": ["E"],
    "E": ["D"]
}


def dfs(graph, vertex, visited):

    visited.add(vertex)

    print(vertex, end=" ")

    for neighbour in graph[vertex]:

        if neighbour not in visited:

            dfs(graph, neighbour, visited)


visited = set()

component_count = 0

print("Connected Components:")

for vertex in graph:

    if vertex not in visited:

        component_count += 1

        print(f"\nComponent {component_count}:")

        dfs(graph, vertex, visited)


print("\n\nTotal Connected Components:", component_count)
