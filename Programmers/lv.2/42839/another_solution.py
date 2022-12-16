def solution(numbers):
    l = len(numbers)

    def get_number_set(number=[], visited=set(), number_set=set()):
        for i in range(l):
            if i not in visited:
                number_set.add(int(''.join(number + [str(numbers[i])])))
                number_set = number_set.union(get_number_set(
                    number=number + [str(numbers[i])],
                    visited=visited.union([i]),
                    number_set=number_set
                ))
        return number_set

    answer = 0
    for number in get_number_set():
        if is_prime(number):
            answer += 1

    return answer
