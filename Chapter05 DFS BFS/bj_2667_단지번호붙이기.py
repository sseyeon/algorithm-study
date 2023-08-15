# 1은 집이 있는 곳을, 0은 집이 없는 곳
n = int(input())
m = 0
count = 0
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    if m == 0:
        m = len(graph[i])

def dfs(x, y):
    if x < 0 or x >= n  or y < 0 or y >= m:
        return False
    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        dfs(x -1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

result = 0
house = []
for i in range(n):
    for j in range(len(graph[i])):
        if dfs(i, j) == True:
            house.append(count)
            result += 1
            count = 0
house.sort()
print(result)
for i in house:
    print(i)