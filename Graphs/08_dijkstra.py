graph = {
    "A": {
        "B": 4,
        "C": 1
    },

    "B": {
        "A": 4,
        "D": 2
    },

    "C": {
        "A": 1,
        "D": 3
    },

    "D": {
        "B": 2,
        "C": 3
    }
}


def dijkstra(graph, start):

    # Set initial distances to infinity
    distance = {}

    for vertex in graph:
        distance[vertex] = float("inf")

    # Distance from start to itself is 0
    distance[start] = 0

    # Keep track of visited vertices
    visited = set()

    while len(visited) < len(graph):

        # Find the unvisited vertex
        # with the smallest distance

        current = None

        for vertex in graph:

            if vertex not in visited:

                if current is None or distance[vertex] < distance[current]:

                    current = vertex

        # Mark current vertex as visited
        visited.add(current)

        # Update neighbouring vertices
        for neighbour, weight in graph[current].items():

            new_distance = distance[current] + weight

            if new_distance < distance[neighbour]:

                distance[neighbour] = new_distance

    return distance


print("Shortest distances from A:")

result = dijkstra(graph, "A")

for vertex, distance in result.items():

    print(vertex, "=", distance)