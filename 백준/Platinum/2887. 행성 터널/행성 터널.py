# 행성 터널
import copy
import heapq
import sys
input = sys.stdin.readline

N = int(input())
planets = []
for i in range(N):
    x, y, z = map(int, input().split())
    planets.append((x, y, z, i))

planets_x = copy.deepcopy(planets)
planets_y = copy.deepcopy(planets)
planets_z = copy.deepcopy(planets)
planets_x.sort(key=lambda index: index[0])
planets_y.sort(key=lambda index: index[1])
planets_z.sort(key=lambda index: index[2])

arr = [[] for _ in range(N)]
for i in range(1, N):
    a, b, c, i1 = planets_x[i-1]
    x, y, z, i2 = planets_x[i]
    cost = min(abs(a-x), abs(b-y), abs(c-z))
    arr[i1].append((cost, i2))
    arr[i2].append((cost, i1))

    a, b, c, i1 = planets_y[i-1]
    x, y, z, i2 = planets_y[i]
    cost = min(abs(a-x), abs(b-y), abs(c-z))
    arr[i1].append((cost, i2))
    arr[i2].append((cost, i1))

    a, b, c, i1 = planets_z[i-1]
    x, y, z, i2 = planets_z[i]
    cost = min(abs(a-x), abs(b-y), abs(c-z))
    arr[i1].append((cost, i2))
    arr[i2].append((cost, i1))


def prim(start):
    global result
    q = []
    heapq.heappush(q, (0, start))
    visited = [False] * N
    count = 0
    while q:
        if count == N:
            break
        cost, node = heapq.heappop(q)
        if not visited[node]:
            count += 1
            result += cost
            visited[node] = True
            for ncost, nnode in arr[node]:
                heapq.heappush(q, (ncost, nnode))


result = 0
prim(0)
print(result)