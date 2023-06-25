import sys

number = [str(i) for i in range(0, 10)]
smallAlphabet = [chr(i) for i in range(97, 123)]
largeAlphabet = [chr(i) for i in range(65, 91)]

while True:
    data = list(map(str, sys.stdin.readline()))
    blank = 0
    count = 0
    small = 0
    large = 0
    if len(data) == 0:
        break
    for i in data:
        if i == " ":
            blank += 1
        if i in largeAlphabet:
            large += 1
        if i in smallAlphabet:
            small += 1
        if i in number:
            count += 1

    print(small, large, count, blank)