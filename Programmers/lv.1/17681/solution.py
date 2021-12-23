def solution(n, arr1, arr2):
    answer = []
    for x1, x2 in zip(arr1, arr2):
        s = bin(x1 | x2)[2:].replace('0', ' ').replace('1', '#')
        s = ' '*(n - len(s)) + s
        answer.append(s)
    
    return answer
