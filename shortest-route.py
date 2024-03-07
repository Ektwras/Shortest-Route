# Σοφιανόπουλος Έκτορας
# Σάββας Κοντόπουλος
# Αντώνης Μιλαθιανάκης
from collections import defaultdict
import heapq


def read_graph(filename):
    graph = defaultdict(dict)
    all_nodes = set()
    start_node = end_node = None

    with open(filename, 'r') as file:
        lines = file.readlines()

        for line in lines[:-2]:
            start, end, weight = line.strip().split()
            graph[start][end] = int(weight)
            all_nodes.update([start, end])

        start_node = lines[-2].strip()
        end_node = lines[-1].strip()

    return graph, all_nodes, start_node, end_node


def dijkstras(graph, nodes, start, end):
    shortest_paths = {vertex: float('infinity') for vertex in nodes}
    shortest_paths[start] = 0
    previous_nodes = {vertex: None for vertex in nodes}
    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > shortest_paths[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                previous_nodes[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.reverse()

    return shortest_paths[end], path if path[0] == start else []


if __name__ == "__main__":
    input_filename = 'input2.txt'
    output_filename = 'output2.txt'

    graph, nodes, start_node, end_node = read_graph(input_filename)

    if start_node not in nodes or end_node not in nodes:
        print(f"Error: Start or end node is not in the graph.")
    else:
        shortest_distance, path = dijkstras(graph, nodes, start_node, end_node)
        with open(output_filename, 'w') as file:
            if path:
                file.write(f"Shortest path from {start_node} to {end_node}: {' -> '.join(path)}\n")
                file.write(f"Total distance: {shortest_distance}\n")
            else:
                file.write(f"No path found from {start_node} to {end_node}\n")
