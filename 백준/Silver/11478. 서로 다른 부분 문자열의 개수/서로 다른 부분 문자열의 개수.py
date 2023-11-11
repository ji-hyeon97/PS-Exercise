import sys

s = sys.stdin.readline().rstrip()
dic = {}
for i in range(len(s)):
    for j in range(i, len(s) + 1):
        data = s[i:j + 1]
        dic[data] = 1
print(len(dic))