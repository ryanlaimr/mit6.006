'''
Implementation of Dijkstra's algorithm in Python using adjacency matrix representation of graphs.

'''
import sys
# Dijkstra's algorithm for finding the shortest path from a vertex to all other vertices in a graph
def dijkstra(graph, start):
    # Initialize distances and visited array
    distances = [sys.maxsize] * len(graph)
    distances[start] = 0
    visited = [False] * len(graph)

    for _ in range(len(graph)):
        # Find the vertex with the minimum distance
        min_dist = sys.maxsize
        min_vertex = -1
        for v in range(len(graph)):
            if not visited[v] and distances[v] < min_dist:
                min_dist = distances[v]
                min_vertex = v

        # Mark the vertex as visited
        visited[min_vertex] = True

        # Update distances of adjacent vertices
        for v in range(len(graph)):
            if not visited[v] and graph[min_vertex][v] != 0:
                new_dist = distances[min_vertex] + graph[min_vertex][v]
                if new_dist < distances[v]:
                    distances[v] = new_dist

    return distances

# Example usage
graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

start_vertex = 0
distances = dijkstra(graph, start_vertex)
print("Shortest distances from vertex", start_vertex)
for i, dist in enumerate(distances):
    print("Vertex", i, ":", dist)
