def solution(surveys, choices):
    scores = {'RT': {'R': 0, 'T': 0},
    'CF': {'C': 0, 'F': 0},
    'MJ': {'M': 0, 'J': 0},
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
    for key in scores:
        a = scores[key][key[0]] # R, C, M, A
        b = scores[key][key[1]] # T, F, J, N
        if score != 'MJ':
            answer.append(score[0] if a >= b else score[1])
        else:
            answer.append(score[1] if a <= b else score[0])

    return ''.join(answer)
