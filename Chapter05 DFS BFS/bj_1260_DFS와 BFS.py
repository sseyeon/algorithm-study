from collections import deque
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
n, m, v = map(int, input().split())
# 그래프 초기화
graph = [[] for i in range(n+1)]
visited_dfs = [0] * (n + 1)
visited_bfs = [0] * (n + 1)
result_dfs = []
result_bfs = []
# 그래프 데이터 생성
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
    

def dfs(v):
    visited_dfs[v] = 1
    result_dfs.append(str(v))
    for nx in graph[v]:
        if visited_dfs[nx] == 0:
            dfs(nx)
        
def bfs(v):
    queue = deque()
    queue.append(v)
    visited_bfs[v] = 1
    while queue:
        c = queue.popleft()
        result_bfs.append(str(c))
        for nx in graph[c]:
            if visited_bfs[nx] == 0:
                visited_bfs[nx] = 1
                queue.append(nx)
dfs(v)
bfs(v)
print(' '.join(result_dfs))
print(' '.join(result_bfs))