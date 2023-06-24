import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(str, sys.stdin.readline().rstrip()))

alphabet = [chr(i) for i in range(65, 91)]

value = []
for _ in range(n):
    value.append(int(sys.stdin.readline().rstrip()))

stack = []

for i in data:
    if i == "*":
        one = stack.pop()
        two = stack.pop()
        if one in alphabet:
            one = value[ord(one) - 65]
        if two in alphabet:
            two = value[ord(two) - 65]
        result = two * one
        stack.append(result)

    if i == "+":
        one = stack.pop()
        two = stack.pop()
        if one in alphabet:
            one = value[ord(one) - 65]
        if two in alphabet:
            two = value[ord(two) - 65]
        result = one + two
        stack.append(result)

    if i == "-":
        one = stack.pop()
        two = stack.pop()
        if one in alphabet:
            one = value[ord(one) - 65]
        if two in alphabet:
            two = value[ord(two) - 65]
        result = two - one
        stack.append(result)

    if i == "/":
        one = stack.pop()
        two = stack.pop()
        if one in alphabet:
            one = value[ord(one) - 65]
        if two in alphabet:
            two = value[ord(two) - 65]
        result = two / one
        stack.append(result)
    if i in alphabet:
        stack.append(i)

print(format(stack[0], ".2f"))