import sys
import heapq
n = int(input())
heap = []
for i in range(n):
    a = (-1) * int(sys.stdin.readline())
    if a == 0:
        if len(heap) == 0:
            print(0)
        else:
            print((-1) * (heapq.heappop(heap)))
    else:
        heapq.heappush(heap, a)