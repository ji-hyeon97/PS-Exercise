def solution(numbers, hand):
    answer = ''
    left = [3,0]
    right = [3,2]
    for i in numbers:
        position = [(i-1)//3, (i-1)%3]
        if i == 0:
            position = [3,1]
        if i in [1,4,7]:
            answer+='L'
            left = position
        if i in [3,6,9]:
            answer+='R'
            right = position
        if i in [2,5,8,0]:
            dl = abs(left[0] - position[0]) + abs(left[1] - position[1])
            dr = abs(right[0] - position[0]) + abs(right[1] - position[1])
            if dl < dr:
                left = position
                answer+='L'
            if dl > dr:
                right = position
                answer+='R'
            if dl == dr:
                if hand[0] == 'l':
                    left = position
                    answer+='L'
                else:
                    right = position
                    answer+='R'
    return answer