# https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            temp = numbers[i] + numbers[j]
            if temp not in answer:
                answer.add(temp)
        
    return sorted(answer)
