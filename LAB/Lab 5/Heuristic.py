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
    'X': {'Y': 2, 'Z': 3},
    'Y': {'X': 2, 'Z': 4, 'W': 5},
    'Z': {'X': 3, 'Y': 4, 'W': 1},
    'W': {'Y': 5, 'Z': 1, 'V': 2},
    'V': {'W': 2}
}

node_value = {
    'X': 2,
    'Y': 3,
    'Z': 1,
    'W': 2,
    'V': 4
}


# Create the graph object
g = Graph(graph, node_value)

# Example usage:
if __name__ == "__main__":
    start_node = 'V'
    end_node = 'X'
    path = g.astar(start_node, end_node)

    print("A* Path from", start_node, "to", end_node, ":", path)
