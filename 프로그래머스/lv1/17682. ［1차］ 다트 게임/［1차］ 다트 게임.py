def solution(dartResult):
    answer = 0
    num = ['0','1','2','3','4','5','6','7','8','9','t']
    stack = []
    dartResult = dartResult.replace('10','t')
    for i in dartResult:
        if i in num:
            if i=='t':
                stack.append(10)
            else:
                stack.append(int(i))
        if i == 'S':
            pass
        if i == 'D':
            data = stack.pop()
            data = data**2
            stack.append(data)
        if i == 'T':
            data = stack.pop()
            data = data**3
            stack.append(data)
        if i == '#':
            stack[-1] = -stack[-1]
        if i == '*':
            data1 = stack.pop()
            data1 = data1 * 2
            if len(stack) >=1:
                data2 = stack.pop()
                data2 = data2 * 2
                stack.append(data2)
            stack.append(data1)
    answer = sum(stack)
    return answer