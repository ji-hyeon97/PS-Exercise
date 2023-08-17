def solution(n):
    n = str(n)
    n=list(map(int, n))
    n.reverse()
    d=len(n)-1

    count=0
    for i in range(d):
        if n[i]>=6:
            count=count+10-n[i]
            n[i+1]=n[i+1]+1
        elif n[i]==5:
            count=count+5
            if n[i+1]>=5:
                n[i+1]=n[i+1]+1
        else:
            count=count+n[i]
    if n[-1]>=6:
        count=count+10-n[-1]+1
    else:
        count=count+n[-1]

    return count