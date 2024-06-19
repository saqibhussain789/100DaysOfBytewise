import heapq

def dijkstra(graph, start):
    queue = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances

# Take input from user
graph = {}
edges = input("Enter the edges with weights (format: u v w) separated by commas: ").split(',')
for edge in edges:
    u, v, w = edge.split()
    w = int(w)
    if u not in graph:
        graph[u] = {}
    if v not in graph:
        graph[v] = {}
    graph[u][v] = w
    # Uncomment the following line if the graph is undirected
    # graph[v][u] = w

start_node = input("Enter the starting node: ")

distances = dijkstra(graph, start_node)
print(f"Shortest distances from node {start_node}: {distances}")
