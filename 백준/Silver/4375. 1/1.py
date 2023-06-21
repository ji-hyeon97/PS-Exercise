import sys

data = 1

while True:
    try:
        n = int(sys.stdin.readline().rstrip())
    except:
        break

    while True:
        if data % n == 0:
            print(len(str(data)))
            data = 1
            break
        else:
            data = data*10 + 1