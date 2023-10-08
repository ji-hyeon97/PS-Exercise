import sys

n = int(sys.stdin.readline().rstrip())
number = list(map(int, sys.stdin.readline().split()))
plus, minus, mul, div = map(int, sys.stdin.readline().split())

mx = -int(1e9)
mn = int(1e9)


def dfs(idx, temp, plus, minus, mul, div):
    global mx, mn
    if temp > int(1e9) or temp < -int(1e9):
        return
    if idx == n:
        mx = max(mx, temp)
        mn = min(mn, temp)
    if plus > 0:
        dfs(idx + 1, temp + number[idx], plus - 1, minus, mul, div)
    if minus > 0:
        dfs(idx + 1, temp - number[idx], plus, minus - 1, mul, div)
    if mul > 0:
        dfs(idx + 1, temp * number[idx], plus, minus, mul - 1, div)
    if div > 0:
        dfs(idx + 1, int(temp / number[idx]), plus, minus, mul, div - 1)


dfs(1, number[0], plus, minus, mul, div)
print(mx)
print(mn)