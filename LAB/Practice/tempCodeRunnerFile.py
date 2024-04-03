def ucs(graph,start,end):
#     visited=set()
#     queue=[(0,start,[start])] 
#     heapq.heapify(queue) 
#     while queue:
#         cost,current,path=heapq.heappop(queue)
#         print(queue)
#         if current==end:
#             return path
#         if current not in visited:
#             visited.add(current)
#             for neighbor,edge_cost in graph[current].items():
#                 if neighbor not in visited:
#                     heapq.heappush(queue,(cost+edge_cost,neighbor,path + [neighbor]))
#             heapq.heapify(queue) 