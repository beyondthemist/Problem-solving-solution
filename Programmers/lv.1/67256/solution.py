#https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    keypad = [['1', '2', '3'],
              ['4', '5', '6'],
              ['7', '8', '9'],
              ['*', '0', '#']]
    
    #initial location
    right_loc = (3, 0)
    left_loc = (3, 2)
    
    dic = {'right': 'R', 'left': 'L'}
    
    for i in range(len(numbers)):
        legal = 'left'
        if numbers[i]%3 == 0 and numbers[i] != 0: #3, 6, 9
            legal = 'right'
        elif numbers[i]%3 == 1: #1, 4, 7
            legal = 'left'
        else: #2, 5, 8, 0
            #Manhattan distance
            left_dist = abs(left[0] - idx[0]) + abs(left[1] - idx[1])
            right_dist = abs(right[0] - idx[0]) + abs(right[1] - idx[1])
            
            if left_dist > right_dist:
                legal = 'right'
            elif left_dist == right_dist:
                legal = hand
        
        if legal == right_loc:
            right_loc = idx
        else:
            left_loc = idx
        
        answer += dic[legal]
            
    return answer
