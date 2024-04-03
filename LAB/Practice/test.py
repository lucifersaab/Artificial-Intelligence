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
    queue=[(node_value[start]+0,start,[start])]  # (total_cost, node, path)
    heapq.heapify(queue) 
    while queue:
        cost,current,path=heapq.heappop(queue)  # we won't be using the cost here
        if current==end:
            return path
        if current not in visited:
            visited.add(current)
            for neighbor,edge_cost in graph[current].items(): # we won't be using the edge_cost here
                if neighbor not in visited:
                    heapq.heappush(queue,((node_value[neighbor]+cost+edge_cost),neighbor,path + [neighbor])) # used total cost here by adding heuristics, edge_cost and previous cost
            heapq.heapify(queue)
    return None

graph = {
    'S': {'A': 5, 'B': 3},
    'A': {'S': 5, 'B': 2, 'C': 4},
    'B': {'S': 3, 'A': 2, 'D': 7},
    'C': {'A': 4, 'D': 6, 'G': 8},
    'D': {'B': 7, 'C': 6, 'G': 9},
    'G': {'C': 8, 'D': 9}
}

node_value = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 3,
    'D': 1,
    'G': 0
}


bfs_path=bfs(graph,'S','G')
dfs_path=dfs(graph,'S','G')
print(bfs_path)
print(dfs_path)

ucs_path=ucs(graph,'S','G')
print(ucs_path)

astar_path=astar(graph,'S','D')
print(astar_path)