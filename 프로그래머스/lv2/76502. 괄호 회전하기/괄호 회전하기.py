def solution(s):
    answer = 0
    for i in range(len(s)):
        stack = []
        data = s[i:] + s[:i]
        for i in data:
            if i == '(' or i=='{' or i=='[':
                stack.append(i)
            if i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(i)
            if i == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(i)
            if i == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(i)
        if len(stack) == 0:
            answer+=1
    return answer