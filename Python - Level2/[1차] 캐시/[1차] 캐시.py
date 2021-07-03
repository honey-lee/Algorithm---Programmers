"""
cache miss - 5
cache hit - 1

["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
   5         5       5         5        5      5         5        5        5        5

"""
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    Q = deque()

    for i in range(len(cities)):
        if cities[i].lower() not in Q and len(Q) < cacheSize:
            Q.append(cities[i].lower())
            answer += 5
        elif cities[i].lower() not in Q and len(Q) >= cacheSize:
            Q.append(cities[i].lower())
            Q.popleft()
            answer += 5
        elif cities[i].lower() in Q:
            """
            LRU 알고리즘
            """
            Q.remove(cities[i].lower())
            Q.append(cities[i].lower())
            answer += 1

    return answer


cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

print(solution(cacheSize, cities))