def solution(babbling):
    answer = 0
    l1 = ['aya', 'ye', 'woo', 'ma']
    l2 = ['ayaaya', 'yeye', 'woowoo', 'mama']

    for b in babbling:
        flag = True
        for x in l2:
            if x in b:
                flag = False
                break

        if flag:
            leng = 0
            for x in l1:
                leng += len(x)*b.count(x)
            if leng == len(b):
                answer += 1
        
    return answer
