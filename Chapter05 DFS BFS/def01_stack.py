stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.pop()
stack.append(7)

print(stack)    # 최하단 원소부터 출력
print(stack[::-1])  # 최상단 원소부터 출력