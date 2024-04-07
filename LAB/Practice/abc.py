import heapq
import time
import sys
import matplotlib.pyplot as plt

def isSafe(board, row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def printSolution(board):
    N = len(board)
    for row in board:
        print(" ".join(["Q" if c == row else "." for c in range(N)]))
    print("\n")

def heuristic(board):
    N = len(board)
    h = 0
    for i in range(N):
        if board[i] == -1: continue
        for j in range(i + 1, N):
            if board[j] == -1: continue
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j): h += 1
    return h

def measure(func, N):
    start_time = time.time()
    solution, space_used = func(N)
    end_time = time.time()
    if solution:
        print(f"{func.__name__} Solution (Time taken: {end_time - start_time}s, Space used: {space_used} bytes):")
        printSolution(solution)
    return end_time - start_time, space_used

def solveNQueens_DFS(N):
    def dfs(col):
        if col == N: return board[:]
        for row in range(N):
            if isSafe(board, row, col):
                board[col] = row
                solution = dfs(col + 1)
                if solution: return solution
                board[col] = -1
        return None
    board = [-1] * N
    solution = dfs(0)
    space_used = sys.getsizeof(board)
    return solution, space_used

def solveNQueens_BFS(N):
    queue = [([-1] * N, 0)]
    while queue:
        board, col = queue.pop(0)
        if col == N: return board, sys.getsizeof(queue)
        for row in range(N):
            if isSafe(board, row, col):
                new_board = board[:]
                new_board[col] = row
                queue.append((new_board, col + 1))
    return None, sys.getsizeof(queue)

def solveNQueens_UCS(N):
    heap = [((0, [-1] * N, 0))]  # (cost, board, col)
    while heap:
        cost, board, col = heapq.heappop(heap)
        if col == N: return board, sys.getsizeof(heap)
        for row in range(N):
            if isSafe(board, row, col):
                new_board = board[:]
                new_board[col] = row
                heapq.heappush(heap, (cost + 1, new_board, col + 1))
    return None, sys.getsizeof(heap)

def solveNQueens_Greedy(N):
    heap = [(heuristic([-1] * N), [-1] * N, 0)]
    while heap:
        h, board, col = heapq.heappop(heap)
        if col == N and h == 0: return board, sys.getsizeof(heap)
        for i in range(N):
            if isSafe(board, i, col):
                new_board = board[:]
                new_board[col] = i
                heapq.heappush(heap, (heuristic(new_board), new_board, col + 1))
    return None, sys.getsizeof(heap)

def solveNQueens_AStar(N):
    heap = [(heuristic([-1] * N), 0, [-1] * N, 0)]
    while heap:
        estimated_cost, path_cost, board, col = heapq.heappop(heap)
        if col == N and estimated_cost == path_cost: return board, sys.getsizeof(heap)
        for row in range(N):
            if isSafe(board, row, col):
                new_board = board[:]
                new_board[col] = row
                new_path_cost = path_cost + 1
                heapq.heappush(heap, (heuristic(new_board) + new_path_cost, new_path_cost, new_board, col + 1))
    return None, sys.getsizeof(heap)

results = {}
N = 8
algorithms = [solveNQueens_DFS, solveNQueens_BFS, solveNQueens_UCS, solveNQueens_Greedy, solveNQueens_AStar]
for algo in algorithms:
    results[algo.__name__] = measure(algo, N)

algos = list(results.keys())
times = [result[0] for result in results.values()]
spaces = [result[1] for result in results.values()]

fig, ax1 = plt.subplots()

color = 'tab:blue'
ax1.set_xlabel('Algorithm')
ax1.set_ylabel('Time Taken (s)', color=color)
ax1.bar(algos, times, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Space Used (bytes)', color=color)
ax2.plot(algos, spaces, color=color, marker='o', linestyle='--')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.title('Algorithm Comparison: Time Taken and Space Used')
plt.show()
