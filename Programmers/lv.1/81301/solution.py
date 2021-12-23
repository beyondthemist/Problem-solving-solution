#https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for word in words:
        s = s.replace(word, str(words.index(word)))

    answer = int(s)
    return answer
