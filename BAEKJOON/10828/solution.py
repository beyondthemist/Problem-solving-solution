import sys

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    cmd = sys.stdin.readline().strip() #readline() contains line feed
    if cmd == 'pop':
        print(stack.pop() if len(stack) > 0 else -1)
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        print(int(len(stack) == 0))
    elif cmd == 'top':
        print(stack[-1] if len(stack) != 0 else -1)
    else:
        stack.append(cmd[5: ])
