graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}


def topological_sort(graph):

    visited = set()

    stack = []

    def dfs(vertex):

        visited.add(vertex)

        for neighbour in graph[vertex]:

            if neighbour not in visited:

                dfs(neighbour)

        # Add vertex AFTER visiting neighbours
        stack.append(vertex)

    for vertex in graph:

        if vertex not in visited:

            dfs(vertex)

    # Reverse the stack
    stack.reverse()

    return stack


result = topological_sort(graph)

print("Topological Order:")

print(" → ".join(result))