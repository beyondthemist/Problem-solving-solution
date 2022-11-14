import sys 
input = sys.stdin.readline

board = input()
board = board.replace('XXXX', 'AAAA').replace('XX', 'BB')
print(-1 if 'X' in board else board)
