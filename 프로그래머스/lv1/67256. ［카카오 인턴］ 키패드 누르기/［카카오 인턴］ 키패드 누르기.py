def solution(numbers, hand):
    answer = ''
    left = [3,0]
    right = [3,2]
    for i in numbers:
        position = [(i-1)//3, (i-1)%3]
        if i==0:
            position = [3,1]
        if i in [1,4,7]:
            answer+='L'
            left = position
        elif i in [3,6,9]:
            answer+='R'
            right = position
        else:
            dl = abs(position[0] - left[0]) + abs(position[1] - left[1])
            dr = abs(position[0] - right[0]) + abs(position[1] - right[1])
            
            if dl > dr:
                answer+='R'
                right = position
            elif dl < dr:
                answer+='L'
                left = position
            else:
                if hand == 'right':
                    answer+='R'
                    right = position
                else:
                    answer+='L'
                    left = position        
    return answer