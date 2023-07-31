answer = 0

def dfs(numbers,target,L,mid):
    global answer
    if L == len(numbers):
        if mid == target:
            answer+=1
            return
        return
    dfs(numbers,target,L+1,mid+numbers[L])
    dfs(numbers,target,L+1,mid-numbers[L])
            
def solution(numbers, target):
    global answer
    dfs(numbers,target,0,0)
    return answer