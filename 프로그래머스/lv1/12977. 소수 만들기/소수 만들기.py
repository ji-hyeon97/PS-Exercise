from itertools import combinations
import math

def prime(m):
    target= int(math.sqrt(m))+1
    for i in range(2,target):
        if m%i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    
    for i in combinations(nums,3):
        if prime(sum(i)) == 1:
            answer+=1
    return answer