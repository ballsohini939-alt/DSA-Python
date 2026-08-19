# ==========================================
# BELLMAN-FORD SHORTEST PATH ALGORITHM
# ==========================================


graph = {
    "A": {
        "B": 4,
        "C": 2
    },

    "B": {
        "D": -3
    },

    "C": {
        "D": 1
    },

    "D": {}
}


def bellman_ford(graph, start):

    # Create a list of all vertices
    vertices = list(graph.keys())

    # Set initial distances to infinity
    distance = {}

    for vertex in vertices:
        distance[vertex] = float("inf")

    # Distance from start to itself
    distance[start] = 0

    # Relax all edges V - 1 times
    for _ in range(len(vertices) - 1):

        for vertex in graph:

            for neighbour, weight in graph[vertex].items():

                if distance[vertex] != float("inf"):

                    new_distance = distance[vertex] + weight

                    if new_distance < distance[neighbour]:

                        distance[neighbour] = new_distance

    return distance


print("Shortest distances from A:")

result = bellman_ford(graph, "A")

for vertex, distance in result.items():

    print(vertex, "=", distance)