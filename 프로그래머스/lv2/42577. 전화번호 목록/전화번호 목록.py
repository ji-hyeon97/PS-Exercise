def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        first = phone_book[i]
        if phone_book[i][0] != phone_book[i+1][0]:
            first = phone_book[i+1]
            continue
        if first == phone_book[i+1][:len(first)]:
            answer = False
            break
    return answer