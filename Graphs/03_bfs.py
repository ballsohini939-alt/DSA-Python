from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}


def bfs(graph, start):

    visited = set()

    queue = deque()

    queue.append(start)

    visited.add(start)

    while len(queue) > 0:

        vertex = queue.popleft()

        print(vertex)

        for neighbour in graph[vertex]:

            if neighbour not in visited:

                visited.add(neighbour)

                queue.append(neighbour)


print("BFS Traversal:")

bfs(graph, "A")