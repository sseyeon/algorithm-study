# () {} [] 를 포함하고 있는 문자열 s가 주어졌을 때, 괄호가 유효한지 아닌지 판별
def isValid(s):
    stack = []
    for p in s:
        if p == '(':
            stack.append(")")
        elif p == "{":
            stack.append("}")
        elif p == "[":
            stack.append("]")
        elif not stack or stack.pop() != p:
            return False
    return not stack    # 스택이 비면 True 반환