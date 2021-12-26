with open('.\\data.txt') as f:
     print(str(sum([int(line) for line in f]))[:10])
