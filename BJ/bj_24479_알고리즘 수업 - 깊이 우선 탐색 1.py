n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
def dfs(v):
    print(v)
    visited[v] = True
    for i in range(len(graph[v])):
        if visited[graph[v][i]] == False:
            dfs(graph[v][i])
dfs(r)
