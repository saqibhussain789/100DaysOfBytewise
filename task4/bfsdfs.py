from collections import deque, defaultdict

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            queue.extend(graph[vertex] - visited)
    
    return result

def dfs(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            stack.extend(graph[vertex] - visited)
    
    return result

# Take input from user
graph = defaultdict(set)
edges = input("Enter the edges (format: u v) separated by commas: ").split(',')
for edge in edges:
    u, v = map(int, edge.split())
    graph[u].add(v)
    graph[v].add(u)

start_node = int(input("Enter the starting node: "))

print("BFS traversal:", bfs(graph, start_node))
print("DFS traversal:", dfs(graph, start_node))
