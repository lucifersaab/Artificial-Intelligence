import heapq

def bfs(graph,start,end):
    visited=set()
    queue=[(start,[start])]

    while queue:
        node,path=queue.pop(0)
        if(node==end):
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor,path+[neighbor]))
    return None

def astar(graph,start,end):
    visited=set()
    queue=[(node_value[start],0,start,[start])] # (total_cost,g_cost,node,path)
    heapq.heapify(queue)

    while queue:
        total_cost,g_cost,node,path=heapq.heappop(queue)
        if(node==end):
            return path
        if node not in visited:
            visited.add(node)
            for neighbor,cost in graph[node].items():
                if neighbor not in visited:
                    neighbor_g_cost=cost+g_cost # calculate g_cost for neighbor
                    heapq.heappush(queue,(neighbor_g_cost+node_value[neighbor],neighbor_g_cost,neighbor,path+[neighbor])) # update queue
    return None


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

print(astar(graph,'S','G'))