import sys

t = int(sys.stdin.readline())
for _ in range(t):
    stack = [' '] #sentinel

    for c in sys.stdin.readline().rstrip():
        if c == ')' and stack[-1] == '(':
            stack.pop()
            continue
        stack.append(c)
    
    print('YES' if stack == [' '] else 'NO')
