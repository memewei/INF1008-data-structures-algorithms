def graph_coloring(graph, n):
    result = [-1] * n  # Store color of each vertex
    result[0] = 0      # Assign the first color to the first vertex

    def is_safe(v, c, color):
        for i in range(n):
            if graph[v][i] == 1 and color[i] == c:
                return False
        return True

    def solve_util(v, color):
        if v == n:
            return True

        for c in range(max(result) + 2):  # Try all colors from 0 to max used color + 1
            if is_safe(v, c, color):
                color[v] = c

                if solve_util(v + 1, color):
                    return True

                color[v] = -1  # Backtrack and remove the color
        return False

    # Start solving from vertex 0
    solve_util(0, result)

    # Print the result
    print("Vertex\tColor")
    for u in range(n):
        print(f"{u}\t{result[u]}")

    # Print the total number of colors used
    print("Minimum number of colors required:", max(result) + 1)


def main():
    num_edges = int(input("Enter the number of edges: "))
    print("Enter each edge as two space-separated integers (e.g., '0 1'):")
    edges = []
    max_vertex = -1
    for _ in range(num_edges):
        u, v = map(int, input().split())
        edges.append((u, v))
        max_vertex = max(max_vertex, u, v)

    n = max_vertex + 1  # Total number of vertices
    graph = [[0] * n for _ in range(n)]
    for u, v in edges:
        graph[u][v] = 1
        graph[v][u] = 1

    # Perform graph coloring
    graph_coloring(graph, n)


if __name__ == "__main__":
    main()
