n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result, tmp = arr[0], arr[0]
# 1
# 1 + 2
# 1 + 2 + 3
# 1 + 2 + 3 + 3
# 1 + 2 + 3 + 3 + 4
for i in range(1, n):
    tmp = tmp + arr[i]
    result += tmp
print(result)
    