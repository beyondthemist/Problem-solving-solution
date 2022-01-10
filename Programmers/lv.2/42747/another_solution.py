# https://programmers.co.kr/learn/courses/30/lessons/42747

solution = lambda citations: max([min(x) for x in enumerate(sorted(citations, reverse=True), start=1)])
