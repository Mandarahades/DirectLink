from GraphUtils import Graph, Node
from Utils import loadJSONHostLink

graph = Graph()

hosts, links = loadJSONHostLink("topology.json")
# Generate the graph from the data
for host in hosts:
    graph.add_node(Node(host, [], 100.0))


for link in links:
    node, neighbor, port = link[0], link[1], link[2]["port"]
    node_obj = graph.find_node(node)
    neighbor_obj = graph.find_node(neighbor)

    if node_obj and neighbor_obj:
        node_obj.neighbors.append(neighbor_obj.name)
        neighbor_obj.neighbors.append(node_obj.name)

# Example usage of filter_paths_by_energy method
start_node_name = 5
target_node_name = 10
threshold_energy = 50

paths = graph.find_paths(start_node_name, target_node_name)

filtered_paths = graph.filter_paths_by_energy(paths, threshold_energy)
AcceptablePaths = []
print(f"Paths from node {start_node_name} to node {target_node_name} with energy above {threshold_energy}:")
for path in filtered_paths:
    AcceptablePaths.append([node.name for node in path])

#print(f'{paths}')
print(f'{AcceptablePaths}')
Paths = []
print(f"Paths from node {start_node_name} to node {target_node_name} with energy above {threshold_energy}:")
for path in paths:
    Paths.append([node.name for node in path])
print(f'{Paths}')
