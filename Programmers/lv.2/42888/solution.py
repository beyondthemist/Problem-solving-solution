# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    leaved = [] #uid
    changed = {} #uid, name
    users = {} #uid, name
    for r in record: # Update changed names
        data = r.split(' ')

        if data[0] == 'Change':
            changed[data[1]] = data[2]
        elif data[0] == 'Leave':
            leaved.append(data[1])
        elif data[0] == 'Enter':
            users[data[1]] = data[2]
            if data[1] in leaved:
                changed[data[1]] = data[2]

    answer = []
    for i in range(len(record)):
        data = record[i].split(' ')
        
        if data[0] == 'Enter':
            answer.append(changed.get(data[1], data[2]) + "님이 들어왔습니다.")
        elif data[0] == 'Leave':
            answer.append(changed.get(data[1], users.get(data[1])) + "님이 나갔습니다.")

    return answer
