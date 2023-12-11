import heapq
import random
from copy import deepcopy
from Graph import generate_source_sink_graph
from tabulate import tabulate

def ford_fulkerson(graph, source, sink, augmenting_path_algorithm):
    residual_graph = deepcopy(graph)
    row = len(graph)
    parent = [-1]*row
    max_flow = 0
    augmenting_paths = []

    while True:
        augmenting_path = augmenting_path_algorithm(residual_graph, source, sink)
        if not augmenting_path:
            break
        
        augmenting_paths.append(augmenting_path)
        bottleneck_capacity = 500000
        for (u, v, cap) in augmenting_path:
            bottleneck_capacity = min(bottleneck_capacity, residual_graph[u][v])
        if (bottleneck_capacity <= 0):
            break
        max_flow += bottleneck_capacity

        # Update residual capacities
        for (u, v, cap) in augmenting_path:
            residual_graph[u][v] = residual_graph[u][v] - bottleneck_capacity
            residual_graph[v][u] = residual_graph[v][u] + bottleneck_capacity

    # Number of Augmenting Paths
    paths = len(augmenting_paths)
    if paths == 0:
        return max_flow, paths, 0, 0

    # Mean Length (ML)
    total_length = sum(len(path) for path in augmenting_paths)
    mean_length = total_length / paths

    # Mean Proportional Length (MPL)
    max_length = max(len(path) for path in augmenting_paths)
    total_proportional_length = sum(len(path) / max_length for path in augmenting_paths)
    mean_proportional_length = total_proportional_length / paths

    return max_flow, paths, mean_length, mean_proportional_length

def shortest_augmenting_path_old(graph, source, sink):
    pq = [(0, source, [])]
    heapq.heapify(pq)
    visited = set()

    while pq:
        _, current, path = heapq.heappop(pq)
        if current == sink:
            return path

        visited.add(current)
        for neighbor, capacity in enumerate(graph[current]):
            if neighbor not in visited and capacity > 0:
                heapq.heappush(pq, (0, neighbor, path + [(current, neighbor, 1)]))
    return []

def dfs_like(graph, source, sink):
    pq = [(float('inf'), source, [])]
    heapq.heapify(pq)
    visited = set()

    while pq:
        _, current, path = heapq.heappop(pq)
        if current == sink:
            return path

        visited.add(current)
        for neighbor, capacity in enumerate(graph[current]):
            if neighbor not in visited and capacity > 0:
                heapq.heappush(pq, ((-1) * len(path), neighbor, path + [(current, neighbor, capacity)]))
    return []

def max_capacity(graph, source, sink):
    pq = [(-float('inf'), source, [])]
    heapq.heapify(pq)
    visited = set()

    while pq:
        _, current, path = heapq.heappop(pq)
        if current == sink:
            return path

        visited.add(current)
        for neighbor, capacity in enumerate(graph[current]):
            if neighbor not in visited:
                heapq.heappush(pq, (min(-capacity, len(path)), neighbor, path + [(current, neighbor, capacity)]))
    return []

def random_augmenting_path(graph, source, sink):
    pq = [(random.random(), source, [])]
    heapq.heapify(pq)
    visited = set()

    while pq:
        _, current, path = heapq.heappop(pq)
        if current == sink:
            return path

        visited.add(current)
        for neighbor, capacity in enumerate(graph[current]):
            if neighbor not in visited and capacity > 0:
                heapq.heappush(pq, (random.random(), neighbor, path + [(current, neighbor, capacity)]))
    return []

def load_graph_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    first_line = lines[0].strip().split(',')
    n, r, upperCap, source, sink, total_edges = first_line

    adjacency_matrix = [list(map(int, line.strip().split(','))) for line in lines[1:]]

    return adjacency_matrix, int(n), float(r), int(upperCap), int(source), int(sink), int(total_edges)

def run_simulations(graph, n, r, upperCap, source, sink, total_edges):

    sap_flow, sap_paths, sap_mean_length, sap_mean_proportional_length = ford_fulkerson(graph, source, sink, shortest_augmenting_path_old)
    dfs_flow, dfs_paths, dfs_mean_length, dfs_mean_proportional_length = ford_fulkerson(graph, source, sink, dfs_like)
    maxcap_flow, maxcap_paths, maxcap_mean_length, maxcap_mean_proportional_length = ford_fulkerson(graph, source, sink, max_capacity)
    rand_flow, rand_paths, rand_mean_length, rand_mean_proportional_length = ford_fulkerson(graph, source, sink, random_augmenting_path)

    data = [
        ["SAP", n, r, upperCap, sap_paths, sap_mean_length, sap_mean_proportional_length, total_edges, sap_flow],
        ["DFS", n, r, upperCap, dfs_paths, dfs_mean_length, dfs_mean_proportional_length, total_edges, dfs_flow],
        ["MaxCap", n, r, upperCap, maxcap_paths, maxcap_mean_length, maxcap_mean_proportional_length, total_edges, maxcap_flow],
        ["Random", n, r, upperCap, rand_paths, rand_mean_length, rand_mean_proportional_length, total_edges, rand_flow],
    ]
    headers = ["Algorithm", "n", "r", "upperCap", "paths", "ML", "MPL", "total edges", "flow"]
    print(tabulate(data, headers=headers, tablefmt="grid"))

# Example simulations
simulation_values = [
    [100, 0.2, 2],
    [200, 0.2, 2],
    [100, 0.3, 2],
    [200, 0.3, 2],
    [100, 0.2, 50],
    [200, 0.2, 50],
    [100, 0.3, 50],
    [200, 0.3, 50],
    [200, 0.2, 30], # Custom parameters
    [200, 0.25, 30] # Custom parameters
]

for i, (n, r, upperCap) in enumerate(simulation_values):
    generate_source_sink_graph(n, r, upperCap, i)

for i, (n, r, upperCap) in enumerate(simulation_values):
    adjacency_matrix, n, r, upperCap, source, sink, total_edges = load_graph_from_file(f'source_sink_graph_{i}.txt')
    run_simulations(adjacency_matrix, n, r, upperCap, source, sink, total_edges)