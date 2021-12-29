# https://programmers.co.kr/learn/courses/30/lessons/12916

solution = lambda s: s.count('p') + s.count('P') == s.count('y') + s.count('Y')

# or
# solution = lambda s: s.lower().count('p') == s.lower().count('y')
# or
# solution = lambda s: s.upper().count('P') == s.upper().count('Y')
