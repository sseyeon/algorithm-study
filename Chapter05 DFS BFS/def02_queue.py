from collections import deque

# Queue 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(3)
queue.append(5)
queue.append(7)
queue.append(9)
queue.popleft()
queue.append(11)
queue.append(13)
queue.append(15)
queue.popleft()

print(queue)    # 먼저 들어온 순서대로 출력
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue)    # 나중에 들어온 원소부터 출력
print(list(queue)) # 배열 형태로 변환