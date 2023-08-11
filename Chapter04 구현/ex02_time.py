# - 문제
# 정수 N이 입력되면 00시 00분 00초 부터 N시 59분 59초까지의 모든 시각 중에서 
# 3이 하나라도 포함되는 모든 경우의 수를 구하라

# - 입력 예시
# 5

# - 출력 예시
# 11475

# 내 답변
n = int(input())
cnt = 0
for i in range(1, n+1):
    if i in (3, 13, 23):
        cnt += 1 * 3600
    else:
        for j in range(0, 60):
            if j in (3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53):
                cnt += 1 * 60
            else :
                for k in range(0, 60):
                    if k in (3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53):
                        cnt += 1
print(cnt)

# ---------
# 더 나은 답변
# H 를 입력받기 
h = int(input())
count = 0 
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)