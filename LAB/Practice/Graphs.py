def bfs(graph, start, end):
    visited = set()
    queue = [(start, [start])]  # each element is (node, path)

    while queue:
        node, path = queue.pop(0)
        if node == end:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))

    return None

def dfs(graph, start, end, path=[]):
    if start == end:
        return path + [start]
    if start not in graph:
        return None
    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs(graph, neighbor, end, path + [start])
            if new_path:
                return new_path
    return None

# Example usage:
if __name__ == "__main__":
    graph = {
        'S': ['A', 'B'],
        'A': ['S', 'B', 'C'],
        'B': ['S', 'A', 'D'],
        'C': ['A', 'D', 'G'],
        'D': ['B', 'C', 'G'],
        'G': ['C', 'D']
    }
    
    start_node = 'A'
    end_node = 'D'
    
    bfs_path = bfs(graph, start_node, end_node)
    dfs_path = dfs(graph, start_node, end_node)
    
    print("BFS Path from", start_node, "to", end_node, ":", bfs_path)
    print("DFS Path from", start_node, "to", end_node, ":", dfs_path)
