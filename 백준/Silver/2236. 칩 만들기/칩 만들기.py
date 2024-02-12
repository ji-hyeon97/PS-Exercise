import sys

N, K = map(int, input().split())

def inputArr():
    arr = []
    priority = list(map(int,sys.stdin.readline().split()))
    for i in range(len(priority)):
        arr.append((priority[i], i))
    arr.sort()
    return arr

arr = inputArr()

for i in range(K):
    if i >= N:
        print(0)
    else:
        print(arr[N-(i+1)][1] + 1)

for i in range(N):
    for j in range(N):
        if arr[j][1] == i and j >= N-K:
            print(arr[j][1] + 1)
        elif arr[j][1] == i:
            print(0)