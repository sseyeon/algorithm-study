# n번 반복, 현재 몇번째 반복인지, i-2 번째 수, i-1 번째 수
# recursive_function(n, i, g, h)
def recursive_function(n, i, g, h):
    if (n-2) == i:
        return print(g+h)
    i += 1
    recursive_function(n, i, h, g+h)
n = int(input())
if (n < 2):
    print(n)
else : 
    recursive_function(n, 0, 0, 1)