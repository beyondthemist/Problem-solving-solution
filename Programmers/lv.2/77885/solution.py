def solution(numbers):
    answer = []
    for number in numbers:
        if number&1 == 0:
            answer.append(number + 1)
        else:
            if number == 1:
                answer.append(2)
            else:
                b = '0' + bin(number)[2:]
                i = b.rindex('01')
                b = b[:i] + '10' + b[(i + 2):]
                answer.append(int(''.join(b), 2))
            
    return answer
