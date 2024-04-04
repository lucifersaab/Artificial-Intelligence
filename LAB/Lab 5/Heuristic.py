from collections import defaultdict
import heapq

class Graph:
    def __init__(self, graph, node_value):
        self.graph = graph
        self.node_value = node_value

    def astar(self, start, end):
        open_list = [(self.node_value[start], start)]  # (f_cost, node)
        closed_set = set()
        came_from = {}
        g_score = defaultdict(lambda: float('inf'))
        g_score[start] = 0
        f_score = defaultdict(lambda: float('inf'))
        f_score[start] = self.node_value[start]  # Heuristic for start node

        while open_list:
            _, current = heapq.heappop(open_list)

            if current == end:
                path = self.reconstruct_path(came_from, end)
                return path

            closed_set.add(current)

            for neighbor, cost in self.graph[current].items():
                tentative_g_score = g_score[current] + cost

                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + self.node_value[neighbor]  # Update f-score
                    if neighbor not in closed_set:
                        heapq.heappush(open_list, (f_score[neighbor], neighbor))

        return None

    def reconstruct_path(self, came_from, current):
        path = []
        while current in came_from:
            path.insert(0, current)
            current = came_from[current]
        return path

graph = {
    'S': {'A': 2, 'B': 1},
    'A': {'S': 2, 'B': 4, 'C': 8},
    'B': {'S': 1, 'A': 4, 'D': 2},
    'C': {'A': 8, 'D': 7, 'G': 4},
    'D': {'B': 2, 'C': 7, 'G': 1},
    'G': {'C': 4, 'D': 1}}
node_value = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 3,
    'D': 1,
    'G': 0
}


# Create the graph object
g = Graph(graph, node_value)

# Example usage:
if __name__ == "__main__":
    start_node = 'S'
    end_node = 'G'
    path = g.astar(start_node, end_node)

    print("A* Path from", start_node, "to", end_node, ":", path)
