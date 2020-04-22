def solution(phone_book):
    phone_book.sort()
    for i,x in enumerate(phone_book):
        me = len(x)
        if i <len(phone_book)-1 and x == phone_book[i+1][:me]:
            return False
    answer = True
    return answer
