def solution(numbers, k):
    answer = [numbers[0]]
    cnt = 0
    for i in range(1, len(numbers)):
        if answer[-1] <= numbers[i]:
            while answer and answer[-1] < numbers[i] and cnt < k:
                answer.pop()
                cnt += 1
        answer.append(numbers[i])
    
    if k > cnt:
        answer = answer[:-(k - cnt)]
    return ''.join(answer)
