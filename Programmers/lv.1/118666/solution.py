def solution(surveys, choices):
    scores = {'RT': {'R': 0, 'T': 0},
    'CF': {'C': 0, 'F': 0},
    'JM': {'J': 0, 'M': 0},
    'AN': {'A': 0, 'N': 0}}

    keys = set(scores.keys())
    for i in range(len(surveys)):
        if surveys[i] not in keys:
            surveys[i] = surveys[i][1] + surveys[i][0]
            if choices[i] > 4:
                choices[i] -= 4
            else:
                choices[i] = 8 - choices[i]
        elif choices[i] < 4:
            choices[i] = 4 - choices[i]
    for survey, choice in zip(surveys, choices):
        scores[survey][survey[choice//4]] += (choice%4)

    answer = []
    for index in scores:
        a = scores[index][index[0]] # R, C, J, A
        b = scores[index][index[1]] # T, F, M, N
        answer.append(score[int(a < b)])
    return ''.join(answer)
