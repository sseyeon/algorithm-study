# - 문제 
# 여러개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장 뽑기 
# 각 행에서 가장 작은 수를 뽑은 후 가장 큰 수를 출력함 

# - 입력 예시 
# 3 3 
# 3 1 2
# 4 1 4
# 2 2 2

# - 출력 예시
# 2

n, m = map(int, input().split())
min_arr = []
for i in range(n):
    arr = list(map(int, input().split()))
    min_arr.append(min(arr))    # 현재 줄에서 가장 작은 수 찾기

print(max(min_arr)) # 답안 출력