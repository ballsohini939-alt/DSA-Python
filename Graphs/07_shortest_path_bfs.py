# ==========================================
# SHORTEST PATH IN AN UNWEIGHTED GRAPH
# USING BFS
# ==========================================


from collections import deque


graph = {
    "A": ["B"],
    "B": ["A", "C", "D"],
    "C": ["B"],
    "D": ["B"]
}


def shortest_path(graph, start, target):

    queue = deque()

    visited = set()

    distance = {}

    queue.append(start)

    visited.add(start)

    distance[start] = 0

    while queue:

        vertex = queue.popleft()

        if vertex == target:
            return distance[vertex]

        for neighbour in graph[vertex]:

            if neighbour not in visited:

                visited.add(neighbour)

                distance[neighbour] = distance[vertex] + 1

                queue.append(neighbour)

    return -1


start = "A"
target = "D"

result = shortest_path(graph, start, target)

print("Starting Vertex:", start)
print("Target Vertex:", target)
print("Shortest Distance:", result)
