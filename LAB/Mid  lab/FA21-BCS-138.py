import heapq
def bfs(graph, start, goal):
    queue = [(start, [start])] 
    paths_list=[]
    visited=set()
    while queue:
        current_node, path = queue.pop(0)
        if current_node == goal:
            paths_list.append(path)
        if current_node not in visited:
            for neighbor in graph[current_node]:
                if neighbor not in path: 
                    queue.append((neighbor, path + [neighbor]))
    return paths_list



def astar(graph,start,end):
    visited=set()
    queue=[(heauristics_value[start],0,start,[start])] 
    heapq.heapify(queue)
    # Total_cost=dict()
    # Total_cost[start]=heauristics_value[start]

    while queue:
        current_total_cost,g_cost,node,path=heapq.heappop(queue)
        if(node==end):
            return path,current_total_cost
        if node not in visited:
            visited.add(node)
            for neighbor,cost in graph[node].items():
                if neighbor not in visited:
                    neighbor_g_cost=cost+g_cost 
                    print(neighbor,heauristics_value[neighbor]+neighbor_g_cost)
                    heapq.heappush(queue,(heauristics_value[neighbor]+neighbor_g_cost,neighbor_g_cost,neighbor,path+[neighbor])) 
    return None


graph1={
    'A':{'B','C','D'},
    'B':{'A','E'},
    'C':{'A','E','F'},
    'D':{'A','G'},
    'E':{'B','C'},
    'F':{'C','G','H','I'},
    'G':{'D','F','J'},
    'H':{'F'},
    'I':{'F'},
    'J':{'G'},
    
}

graph2={
    'A':{'B':6,'C':9,'E':1},
    'B':{'A':6,'D':3,'E':4},
    'C':{'A':9,'F':2,'G':3},
    'D':{'B':3,'E':5,'F':7},
    'E':{'A':1,'B':4,'D':5,'F':6},
    'F':{'C':2,'D':7,'E':6},
    'G':{'C':3}
}
heauristics_value={
    'A':7,
    'B':5,
    'C':5,
    'D':6,
    'E':5,
    'F':4,
    'G':0
}

print("----QUESTION 1----")

bfs_path=bfs(graph1,'A','I')
print(bfs_path)
print("\n")

print("----QUESTION 2----")
astar_path,astar_cost=astar(graph2,'A','G')
print("Path from A -> G: ", astar_path)
print("Cost for the path: ",astar_cost)
print("\n")
