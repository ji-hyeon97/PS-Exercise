import sys

E, S, M = map(int, sys.stdin.readline().split())
e, s, m, year = 1, 1, 1, 1

while True:
    if E == e and S == s and M == m:
        print(year)
        break
    else:
        e += 1
        s += 1
        m += 1
        year += 1
        if e > 15:
            e = 1
        if s > 28:
            s = 1
        if m > 19:
            m = 1