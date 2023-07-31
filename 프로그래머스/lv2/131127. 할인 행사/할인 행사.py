import collections
def solution(want, number, discount):
    answer = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]
    
    for i in range(len(discount)-9):
        sale = collections.defaultdict(int)
        for j in range(i,i+10):
            sale[discount[j]] +=1
        if dic == sale:
            answer+=1
    return answer