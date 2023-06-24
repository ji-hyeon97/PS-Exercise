import sys

n = int(sys.stdin.readline().rstrip())
length = len(str(n))
answer = 0

for i in range(1, length + 1):
    if length == 1:
        answer = n
    elif length == 2:
        answer = 9 + 2 * (n - 9)
    elif length == 3:
        answer = 9 + 2 * 90 + 3 * (n - 99)
    elif length == 4:
        answer = 9 + 2 * 90 + 3 * 900 + 4 * (n - 999)
    elif length == 5:
        answer = 9 + 2 * 90 + 3 * 900 + 4 * 9000 + 5 * (n - 9999)
    elif length == 6:
        answer = 9 + 2 * 90 + 3 * 900 + 4 * 9000 + + 5 * 90000 + 6 * (n - 99999)
    elif length == 7:
        answer = 9 + 2 * 90 + 3 * 900 + 4 * 9000 + + 5 * 90000 + 6 * 900000 + 7 * (n - 999999)
    elif length == 8:
        answer = 9 + 2 * 90 + 3 * 900 + 4 * 9000 + + 5 * 90000 + 6 * 900000 + 7 * 9000000 + 8 * (n - 9999999)
    elif length == 9:
        answer = 9 + 2 * 90 + 3 * 900 + 4 * 9000 + + 5 * 90000 + 6 * 900000 + 7 * 9000000 + 8 * 90000000 + 9 * (
                    n - 99999999)
print(answer)