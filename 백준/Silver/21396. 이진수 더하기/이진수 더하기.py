import sys
from collections import defaultdict

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    m = defaultdict(int)
    ans = 0

    data = list(map(int, sys.stdin.readline().split()))

    for i in range(N):
        ans += m[data[i]]
        m[data[i] ^ M] += 1
    print(ans)