# https://programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    hit = 1; miss = 5
    if cacheSize == 0:
        return len(cities) * miss
    
    cities = [city.upper() for city in cities]
    cache = []
    time = 0
    for city in cities:
        if city in cache:
            time += hit
            cache.remove(city)
            cache.append(city)
        else:
            if len(cache) >= cacheSize:
                cache.pop(0)
            cache.append(city)
            time += miss
            
    return time
