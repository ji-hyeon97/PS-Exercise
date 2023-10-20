import sys

n = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(100)]

for _ in range(n):
    root, child1, child2 = map(str, sys.stdin.readline().split())
    graph[ord(root)].append(ord(child1))
    graph[ord(root)].append(ord(child2))


def preorder(word):
    if word == 46:
        return
    print(chr(word), end="")
    preorder(graph[word][0])
    preorder(graph[word][1])


def inorder(word):
    if word == 46:
        return
    inorder(graph[word][0])
    print(chr(word), end="")
    inorder(graph[word][1])


def postorder(word):
    if word == 46:
        return
    postorder(graph[word][0])
    postorder(graph[word][1])
    print(chr(word), end="")


preorder(65)
print("")
inorder(65)
print('')
postorder(65)