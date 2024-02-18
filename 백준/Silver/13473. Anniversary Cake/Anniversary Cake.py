import sys

w, h, ax, ay, bx, by = map(int, sys.stdin.readline().split())

if ax != bx:
    print(min(ax, bx), 0, max(ax, bx), h)
else:
    print(0, min(ay, by), w, max(ay, by))