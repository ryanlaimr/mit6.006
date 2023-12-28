'''
Implementation of Breadth First Search (BFS) in Python using queue

'''

# Using queue
def bfs_queue(graph, start):
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node)
            visited.add(node)
            neighbors = graph[node]
            queue.extend(neighbors)

# Using adjacency list
def bfs_adjlist(graph, start):
    level = {start: 0}
    parent = {start: None}
    i = 1
    frontier = [start]
    print(start)
    while frontier:
        next = []
        for u in frontier:
            for v in graph[u]:
                if v not in level:
                    print(v)
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next
        i += 1

'''
Time Complexity: O(V+E)
Space Complexity: O(V)
V: Vertices; E: Edges

Do not visit the same vertice twice!

'''

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs_queue(graph, 'A')
bfs_adjlist(graph, 'A')