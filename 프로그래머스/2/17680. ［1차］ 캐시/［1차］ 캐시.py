def solution(cacheSize, cities):
    cache = []
    runtime = 0
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    if cacheSize == 0:
        return len(cities)*5
    for city in cities:
        if not city in cache:
            if len(cache) < cacheSize:
                cache.append(city)
                runtime += 5
            else:
                if cache:
                    cache.pop(0)
                cache.append(city)
                runtime += 5
        else:
            cache.pop(cache.index(city))
            cache.append(city)
            runtime += 1
            
    return runtime