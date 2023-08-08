def solution(book_time):
    answer = 0
    check = [0] * (23*60+59+10)
    for start,end in book_time:
        h,m = start.split(":")
        start = int(h)*60 + int(m)
        h,m = end.split(":")
        end = int(h)*60 + int(m)
        for i in range(start, end+10):
            check[i]+=1
    return max(check)