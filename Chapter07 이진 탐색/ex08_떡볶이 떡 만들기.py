# 입력 예시 
# 4 6
# 19 15 10 17

# Step 1.   시작점은 0, 끝점은 가장 긴 떡의 길이(19)로 설정
#           0과 19의 중간점 9를 절단기 높이로 설정하면 
#           얻을 수 있는 떡의 합은 (10 + 6 + 1 + 8) = 25
#           필요한 떡의 길이가 6보다 크기 때문에 시작점을 증가시킴
# Step 2.   시작점을 10으로 옮김
#           끝점은 여전히 19 이니 중간점은 14
#           떡의 합은 (5 + 1 + 3) = 9
# Step 3.   시작점은 15
#           중간점은 17
#           떡의 합은 2
#           필요한 떡의 길이인 6보다 작기 때문에 끝점을 감소시킴
# Step 4.   시작점 15, 끝점 16 (중간점 - 1), 중간점은 15
#           떡의 합은 6

# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력받기 
n, m = list(map(int, input().split())) 
# 각 떡의 개별 높이 정보를 입력받기
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정 
start = 0 
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
    else :
        result = mid
        start = mid + 1
print(result)