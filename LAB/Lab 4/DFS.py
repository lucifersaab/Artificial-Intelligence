


def dfs(graph, start, target=None):
    visited = [] 
    stack = [(start, [start])] 

    while stack:   
        node, path = stack.pop()  
        if node not in visited:
            visited.append(node)

            if node == target:  
                print("Path found:", ' -> '.join(path))
                return path

            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append((neighbour, path + [neighbour]))

    print("Target node not found!" if target else "")
    return None

print("Following is the Depth-First Search")
graph = {
         "A": ["B", "E", "C"],
         "B": ["A", "E", "D"],
         "C": ["A", "F", "G"],
         "D": ["B", "E"],
         "E": ["A", "B", "D"],
         "F": ["C"],
         "G": ["C"]
         }

start_node = 'A'
target_node = 'F'
path = dfs(graph, start_node, target_node)
