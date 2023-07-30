def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    left = []
    right = []
    temp = ''
    for i in range(len(str1)-1):
        temp += str1[i]+str1[i+1]
        if len(temp) == 2:
            if 97<=ord(temp[0])<=126 and 97<=ord(temp[1])<=122:
                left.append(temp)
                temp=""
            else:
                temp = ""
                
    for i in range(len(str2)-1):
        temp += str2[i]+str2[i+1]
        if len(temp) == 2:
            if 97<=ord(temp[0])<=126 and 97<=ord(temp[1])<=122:
                right.append(temp)
                temp=""
            else:
                temp = ""

    up,down = 0,0
    up = len(left) + len(right)
    for i in left:
        if i in right:
            down+=1
            right.remove(i)
    
    up = up - down
    if up == 0:
        return 65536
    
    return(int((down/up)*65536))