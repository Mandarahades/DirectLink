
from Utils import remove_duplicates
from collections import deque


class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def find_paths(self, start_node_name, target_node_name):
        start_node = self.find_node(start_node_name)
        target_node = self.find_node(target_node_name)

        if not start_node or not target_node:
            return []

        paths = []
        queue = deque([[start_node]])

        while queue:
            path = queue.popleft()
            current_node = path[-1]

            if current_node == target_node:
                paths.append(path)

            for neighbor_name in current_node.neighbors:
                neighbor_node = self.find_node(neighbor_name)

                if neighbor_node and neighbor_node not in path:
                    new_path = path + [neighbor_node]
                    queue.append(new_path)

        return remove_duplicates(paths)

    def find_node(self, node_name):
        for node in self.nodes:
            if node.name == node_name:
                return node
        return None

    def get_node_energy(self, node_name):
        node = self.find_node(node_name)
        if node:
            return node.energy
        return None

    def filter_paths_by_energy(self, paths, threshold_energy):
        filtered_paths = []
        for path in paths:
            energy_valid = True
            for node in path:
                if self.get_node_energy(node.name) < threshold_energy:
                    energy_valid = False
                    break
            if energy_valid:
                filtered_paths.append(path)
        return filtered_paths


class Node:
    def __init__(self, name, neighbors, energy):
        self.name = name
        self.neighbors = neighbors
        self.energy = energy
