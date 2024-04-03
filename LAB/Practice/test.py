import heapq

def bfs(graph,start,end):
    visited=set()
    queue=[(start,[start])]
    
    while queue:
        current,path=queue.pop(0)
        if current==end:
            return path
        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor,path + [neighbor]))
    return None
                
def dfs(graph, start, end):
    visited = set()
    stack = [(start, [start])] #stack instead of queue
    while stack: #stack instead of queue
        current, path = stack.pop(-1) #stack instead of queue and poping from last index
        if current == end:
            return path
        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None

def ucs(graph,start,end):
    visited=set()
    queue=[(0,start,[start])] # adding cost in the queue as well
    heapq.heapify(queue) # heapifying queue to sort it
    while queue:
        cost,current,path=heapq.heappop(queue) # using heap's pop meathod to get smallest value
        if current==end:
            return path
        if current not in visited:
            visited.add(current)
            for neighbor,edge_cost in graph[current].items(): # we check neighbor and neighbor's cost
                if neighbor not in visited:
                    heapq.heappush(queue,(cost+edge_cost,neighbor,path + [neighbor])) # add previous cost + cost to reach the neighbor in queue using heap's push method
            heapq.heapify(queue) # heapify again to sort the queue again after insertion of new nodes above
    return None

def greedy(graph,start,end):
    visited=set()
    queue=[(node_value[start],start,[start])]  # used heuristics value here instead of edge cost (heauristics, node, path)
    heapq.heapify(queue) 
    while queue:
        cost,current,path=heapq.heappop(queue)  # we won't be using the cost here
        if current==end:
            return path
        if current not in visited:
            visited.add(current)
            for neighbor,edge_cost in graph[current].items(): # we won't be using the edge_cost here
                if neighbor not in visited:
                    heapq.heappush(queue,(node_value[neighbor],neighbor,path + [neighbor])) # used heuristics value here instead of cost and edge_cost
            heapq.heapify(queue)
    return None

def astar(graph,start,end):
    visited=set()
    queue=[(node_value[start],0,start,[start])] # (total_cost,g_cost,node,path) 1 more value added to keep record of g_cost for each node
    heapq.heapify(queue)
    while queue:
        total_cost,g_cost,node,path=heapq.heappop(queue) #not using total_cost here, just used for priority queue heapify
        if(node==end):
            return path
        if node not in visited:
            visited.add(node)
            for neighbor,cost in graph[node].items():
                if neighbor not in visited:
                    neighbor_g_cost=cost+g_cost # calculate g_cost for neighbor
                    heapq.heappush(queue,(neighbor_g_cost+node_value[neighbor],neighbor_g_cost,neighbor,path+[neighbor])) # update queue
    return None

# graph = {
#     'S': {'A': 2, 'B': 1},
#     'A': {'S': 2, 'B': 4, 'C': 8},
#     'B': {'S': 1, 'A': 4, 'D': 2},
#     'C': {'A': 8, 'D': 7, 'G': 4},
#     'D': {'B': 2, 'C': 7, 'G': 1},
#     'G': {'C': 4, 'D': 1}}
# node_value = {
#     'S': 7,
#     'A': 6,
#     'B': 2,
#     'C': 3,
#     'D': 1,
#     'G': 0
# }

graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'A': 4, 'C': 2, 'D': 5},
    'C': {'A': 3, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 2},
    'E': {'D': 2}
}

node_value = {
    'A': 3,
    'B': 2,
    'C': 2,
    'D': 1,
    'E': 0
}

bfs_path=bfs(graph,'A','E')
dfs_path=dfs(graph,'A','E')
ucs_path=ucs(graph,'A','E')
greedy_path=greedy(graph,'A','E')
astar_path=astar(graph,'A','E')
print("bfs_path: ",bfs_path)
print("dfs_path: ",dfs_path)
print("ucs_path: ",ucs_path)
print("greedy_path: ",greedy_path)
print("astar_path: ",astar_path)