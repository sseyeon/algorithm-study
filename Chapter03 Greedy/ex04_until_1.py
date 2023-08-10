# - 문제 
# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택해서 수행하려고 한다. 
# 단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다
# N과 K가 주어질 때 N이 1이 될 때까지 수행해야 하는 최소 횟수를 구하라

# - 입력 예시
# 25 5

# - 출력 예시
# 2

n, k = map(int, input().split())
cnt = 0
while n != 1:       # n이 1이 될 때까지 수행
    if n % k == 0:  # 2번 연산
        n //= k
    else :          # 1번 연산
        n -= 1
    cnt += 1
print(cnt)