import heapq

def dijkstra(graph, start):
    # Priority queue to store (distance, vertex) tuples
    priority_queue = [(0, start)]
    # Dictionary to store the shortest distance to each vertex
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example graph represented as an adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Perform Dijkstra's algorithm starting from vertex 'A'
shortest_paths = dijkstra(graph, 'A')
print(shortest_paths)