import sys

n, m, k = map(int, sys.stdin.readline().split())
nStorage = [0]
mStorage = [0]

for _ in range(n):
    temp = int(sys.stdin.readline().rstrip())
    nStorage.append(temp)
for _ in range(m):
    temp = int(sys.stdin.readline().rstrip())
    mStorage.append(temp)
    
x = min(sum(nStorage), sum(mStorage))
nFloor = 1
mFloor = 1

cost = 0
while True:

    if nFloor >= len(nStorage) or mFloor >= len(mStorage):
        break

    if nStorage[nFloor] > mStorage[mFloor]:
        nStorage[nFloor] -= mStorage[mFloor]
        cost += (nFloor + mFloor) * mStorage[mFloor]
        mFloor += 1
        continue

    if nStorage[nFloor] == mStorage[mFloor]:
        cost += (nFloor + mFloor) * mStorage[mFloor]
        mFloor += 1
        nFloor += 1
        continue

    if nStorage[nFloor] < mStorage[mFloor]:
        mStorage[mFloor] -= nStorage[nFloor]
        cost += (nFloor + mFloor) * nStorage[nFloor]
        nFloor += 1

if k == 0:
    print(0, 0)
else:
    print(x, cost)