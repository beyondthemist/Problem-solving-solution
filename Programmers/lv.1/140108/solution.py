def solution(s):
    x = s[0]

    answer = 0
    cnt = [1, 0]
    for i in range(1, len(s)):
        if x == 'X':
            x = s[i]
            cnt[0], cnt[1] = 0, 0

        cnt[int(s[i] != x)] += 1

        if cnt[0] == cnt[1]:
            x = 'X'
            answer += 1


    return answer + int(x != 'X')
