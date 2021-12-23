# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    phone_book = sorted(phone_book)
    
    key = phone_book[0]
    for i in range(1, len(phone_book)):
        if key == phone_book[i][0:len(key)]:
            return False
        else:
            key = phone_book[i]
    return True
