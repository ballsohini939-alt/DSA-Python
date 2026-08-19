INF = float("inf")


vertices = ["A", "B", "C", "D"]


distance = {

    "A": {
        "A": 0,
        "B": 4,
        "C": 1,
        "D": INF
    },

    "B": {
        "A": INF,
        "B": 0,
        "C": INF,
        "D": 2
    },

    "C": {
        "A": INF,
        "B": INF,
        "C": 0,
        "D": 3
    },

    "D": {
        "A": INF,
        "B": INF,
        "C": INF,
        "D": 0
    }
}


for intermediate in vertices:

    for start in vertices:

        for end in vertices:

            new_distance = (
                distance[start][intermediate]
                + distance[intermediate][end]
            )

            if new_distance < distance[start][end]:

                distance[start][end] = new_distance


print("All-Pairs Shortest Distance:")

print("    ", end="")

for vertex in vertices:

    print(f"{vertex:>5}", end="")

print()


for start in vertices:

    print(start, end="   ")

    for end in vertices:

        if distance[start][end] == INF:

            print(f"{'INF':>5}", end="")

        else:

            print(f"{distance[start][end]:>5}", end="")

    print()