data = []
vowel = ['A', 'E', 'I', 'O', 'U']

def dfs(cnt,word,string):
    global data
    if cnt == len(string):
        data.append(string)
        return
    else:
        for i in vowel:
            string+=i
            dfs(cnt,word,string)
            string = string[:-1]

def solution(word):
    global data
    answer = 1
    for i in range(1,6):
        dfs(i,word,'')
    data.sort()
    for i in data:
        if word == i:
            return answer
        else:
            answer+=1
    return answer