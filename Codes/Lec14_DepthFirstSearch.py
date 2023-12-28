'''
Implementation of Depth First Search (DFS) algorithm in Python.


'''

def DFS(graph, start):
    visited = []
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(graph[vertex] - set(visited))

    return visited

# Example
graph = {1: set([2, 3]),
         2: set([1, 4, 5]),
         3: set([1, 6]),
         4: set([2]),
         5: set([2, 6]),
         6: set([3, 5])}

print(DFS(graph, 1))