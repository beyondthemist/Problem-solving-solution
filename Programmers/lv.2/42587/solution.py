https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    items = [] #list of tuple (document, priority)
    for i in range(len(priorities)):
        items.append((i, priorities[i]))
    
    printed = 0
    while len(items) >= 2:
        values = [x[1] for x in items]
        if values[0] < max(values[1:]):
            items.append(items.pop(0))
        else:
            if items[0][0] == location:
                break
            items.pop(0)
            printed += 1
            
    return [x[0] for x in items].index(location) + 1 + printed
