def solution(new_id):
    answer = ''
    
    first = ''
    for i in new_id:
        first+=i.lower()
    
    can = ['-','_','.']
    for i in range(ord('a'),ord('z')+1):
        can.append(chr(i))
    for i in range(0,10):
        can.append(str(i))   
    for i in first:
        if i not in can:
            continue
        answer+=i

    dot = []
    for i in range(16,1,-1):
        dot.append('.'*i)
    for i in dot:
        if i in answer:
            answer = answer.replace(i,'.')
    
    if len(answer) and answer[0] == '.':
        answer = answer[1:]
    if len(answer) and answer[-1] == '.':
        answer = answer[:-1]
    
    if len(answer) == 0:
        answer+='a'
    
    if len(answer) >=16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    if len(answer) <=2:
        while True:
            if len(answer) == 3:
                break
            answer+=answer[-1]

    return answer