import sys

l, c = map(int, sys.stdin.readline().split())
data = list(map(str, sys.stdin.readline().split()))
temp = [ord(i) for i in data]
temp.sort()
check = [0 for _ in range(200)]
password = []
vowel = ['a', 'e', 'i', 'o', 'u']
dic = {}


def backtracking(index):
    if len(password) == l:
        answer = ""
        alphabet_vowel = 0
        alphabet_consonant = 0
        for i in password:
            if chr(i) in vowel:
                alphabet_vowel += 1
            else:
                alphabet_consonant += 1
        if alphabet_consonant >= 2 and alphabet_vowel >= 1:
            for i in password:
                answer += chr(i)
            print(answer)
        return

    for i in range(index, c):
        password.append(temp[i])
        backtracking(i+1)
        password.pop()


backtracking(0)