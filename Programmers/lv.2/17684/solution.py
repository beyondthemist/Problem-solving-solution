def solution(msg):
    answer = []
    d = [chr(c) for c in range(65, 91)]
    l = len(msg)
    i = 0
    while i < l:
        j = i + 1
        x = msg[i:j]
        while j < l and x in d:
            j += 1
            x = msg[i:j]

        if x in d:
            answer.append(d.index(x) + 1)
            break

        d.append(x)
        answer.append(d.index(x[:-1]) + 1)
        i += j - i - 1

    return answer
