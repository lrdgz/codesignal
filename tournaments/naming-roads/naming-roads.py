def namingRoads(r):
    r.sort(key = lambda x: x[2])
    for i in range(len(r) - 1):
        for e in r[i][:2]:
            if e in r[i + 1][:2]:
                return False
    return True

roads = [[0, 1, 0],
         [4, 1, 2],
         [4, 3, 4],
         [2, 3, 1],
         [2, 0, 3]]
         
print(namingRoads(roads))