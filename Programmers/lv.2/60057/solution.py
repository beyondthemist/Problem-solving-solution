#https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    length = len(s)
    answer = length
    for i in range(1, length):
        x = ''
        count = 1
        for j in range(i, len(s) + i, i):                  
            if s[j - i:j] == s[j:j + i]:
                count += 1
            else:
                if count > 1:
                    x += str(count)
                x += s[j - i:j]
                count = 1

        if answer > len(x):
            answer = len(x)

    return answer
