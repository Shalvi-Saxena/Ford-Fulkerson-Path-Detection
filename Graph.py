import random
import csv
from collections import deque

def generate_source_sink_graph(n, r, upper_cap, index):
    vertices = [(random.uniform(0, 1), random.uniform(0, 1)) for _ in range(n)]
    edges = set()
    graph = [[0 for x in range(n)] for y in range(n)] 

    for u in vertices:
        for v in vertices:
            if u != v and (u[0] - v[0])**2 + (u[1] - v[1])**2 <= r**2:
                rand = random.uniform(0, 1)
                if rand < 0.5:
                    if (u, v) not in edges and (v, u) not in edges:
                        edges.add((u, v))
                else:
                    if (u, v) not in edges and (v, u) not in edges:
                        edges.add((v, u))

    # Assign random capacities to edges
    edges_with_capacities = [{'edge': edge, 'cap': random.randint(1, upper_cap)} for edge in edges]
    
    for i, edge_info in enumerate(edges_with_capacities):
        edge = edge_info['edge']
        u=vertices.index(edge[0])
        v=vertices.index(edge[1])
        graph[u][v] = edge_info['cap']
    is_s_t_same = True
    
    while is_s_t_same:
        s = random.randint(0, n - 1)
        t = find_longest_acyclic_path(graph, s)
        is_s_t_same = s==t
    
    write_graph_to_file(graph, n, r, upper_cap, s, t, len(edges_with_capacities), f'source_sink_graph_{index}.txt')
    return graph, s, t

def find_longest_acyclic_path(graph, start):
    visited = [False] * len(graph)
    distance = [0] * len(graph)
    
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()

        for neighbor, capacity in enumerate(graph[current]):
            if capacity > 0 and not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                distance[neighbor] = distance[current] + 1

    # The end node of the longest acyclic path is the one with the maximum distance
    end_node = distance.index(max(distance))
    return end_node

def write_graph_to_file(graph, n, r, upper_cap, source, sink, total_edges, file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([n, r, upper_cap, source, sink, total_edges])
        for row in graph:
            writer.writerow(row)

