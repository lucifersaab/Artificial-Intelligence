from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, cost):
        self.graph[u][v] = cost

    def bfs(self, start, end):
        visited = set()
        queue = [[start, 0]]  # each element is [node, cost]

        while queue:
            path, cost = queue.pop(0)
            vertex = path[-1]

            if vertex == end:
                return path, cost

            if vertex not in visited:
                for neighbor, edge_cost in self.graph[vertex].items():
                    new_path = list(path)
                    new_path.append(neighbor)
                    new_cost = cost + edge_cost
                    queue.append([new_path, new_cost])

                visited.add(vertex)

        return None, None

    def dfs(self, start, end):
        visited = set()

        def dfs_recursive(vertex, path, cost):
            if vertex == end:
                return path + [vertex], cost

            visited.add(vertex)

            for neighbor, edge_cost in self.graph[vertex].items():
                if neighbor not in visited:
                    new_path, new_cost = dfs_recursive(neighbor, path + [vertex], cost + edge_cost)
                    if new_path:
                        return new_path, new_cost

            return None, None

        return dfs_recursive(start, [], 0)

# Example usage:
if __name__ == "__main__":
    g = Graph()
    # g.add_edge('A', 'F', 1)
    # g.add_edge('F', 'A', 1)
    # g.add_edge('F', 'H', 1)
    # g.add_edge('H', 'F', 1)
    # g.add_edge('H', 'I', 1)
    # g.add_edge('H', 'M', 1)
    # g.add_edge('M', 'H', 1)
    # g.add_edge('M', 'N', 1)
    # g.add_edge('M', 'R', 1)
    # g.add_edge('R', 'S', 1)
    # g.add_edge('R', 'M', 1)
    # g.add_edge('I', 'H', 1)
    # g.add_edge('I', 'N', 1)
    # g.add_edge('I', 'J', 1)
    # g.add_edge('N', 'M', 1)
    # g.add_edge('N', 'S', 1)
    # g.add_edge('N', 'I', 1)
    # g.add_edge('S', 'T', 1)
    # g.add_edge('S', 'R', 1)
    # g.add_edge('S', 'N', 1)
    # g.add_edge('B', 'G', 1)
    # g.add_edge('B', 'C', 1)
    
    start_node = 'A'
    end_node = 'D'
    bfs_path, bfs_cost = g.bfs(start_node, end_node)
    dfs_path, dfs_cost = g.dfs(start_node, end_node)

    print("BFS Path from", start_node, "to", end_node, ":", bfs_path, "with cost:", bfs_cost)
    print("DFS Path from", start_node, "to", end_node, ":", dfs_path, "with cost:", dfs_cost)