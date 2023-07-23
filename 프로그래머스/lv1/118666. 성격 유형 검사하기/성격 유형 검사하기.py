def solution(survey, choices):
    answer = ''
    data = {}
    alpha = ['R','T','C','F','J','M','A','N']
    for i in alpha:
        data[i] = 0
    
    for i in range(len(survey)):
        if choices[i] >= 4:
            data[survey[i][1]] += choices[i] - 4
        else:
            data[survey[i][0]] += 4 - choices[i]
    
    if data['R'] >= data['T']:
        answer+='R'
    else:
        answer+='T'
    if data['C'] >= data['F']:
        answer+='C'
    else:
        answer+='F'
    if data['J'] >= data['M']:
        answer+='J'
    else:
        answer+='M'
    if data['A'] >= data['N']:
        answer+='A'
    else:
        answer+='N'
        
    return answer