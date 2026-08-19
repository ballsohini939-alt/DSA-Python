graph = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B"],
    "D": []
}


def has_cycle(graph, vertex, visited, parent):
    visited.add(vertex)
    for neighbour in graph[vertex]:

        # If neighbour is not visited
        if neighbour not in visited:
            if has_cycle(graph, neighbour, visited, vertex):
                return True

        # If neighbour is visited and
        # is not the parent, cycle exists
        elif neighbour != parent:
            return True
    return False


visited = set()
cycle_found = False
for vertex in graph:
    if vertex not in visited:
        if has_cycle(graph, vertex, visited, None):
            cycle_found = True
            break


if cycle_found:
    print("Cycle detected")
else:
    print("No cycle detected")