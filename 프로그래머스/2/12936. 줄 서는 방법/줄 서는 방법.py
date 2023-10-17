def fact(n):
    if n<=0:
        return 1
    else:
        return n*fact(n-1)

def solution(n, k):
    answer = []
    nums = [i for i in range(1,n+1)]
    
    while n>0:
        grade = fact(n-1)
        idx = k//grade
        k = k%grade
        if k==0:
            answer.append(nums.pop(idx-1))
        else:
            answer.append(nums.pop(idx))
        n-=1
    return answer