graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}


def dfs(graph, vertex, visited):
    visited.add(vertex)
    print(vertex)
    for neighbour in graph[vertex]:

        if neighbour not in visited:
            dfs(graph, neighbour, visited)

visited = set()
print("DFS Traversal:")
dfs(graph, "A", visited)