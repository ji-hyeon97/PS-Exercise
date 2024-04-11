T = int(input().rstrip())

dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]

for t in range(T):
    m, a = map(int, input().split())

    userA = (0, 0)
    userB = (9, 9)

    commandA = [0] + list(map(int, input().split()))
    commandB = [0] + list(map(int, input().split()))

    charge = []
    for _ in range(a):
        charge.append(list(map(int, input().split())))

    charge.sort(key=lambda v: v[3], reverse=True)

    amountA = 0
    amountB = 0

    for i in range(m + 1):
        nxA = userA[0] + dx[commandA[i]]
        nyA = userA[1] + dy[commandA[i]]
        userA = (nxA, nyA)

        nxB = userB[0] + dx[commandB[i]]
        nyB = userB[1] + dy[commandB[i]]
        userB = (nxB, nyB)

        possibleA = []
        possibleB = []
        index = 0
        for b, a, c, d in charge:
            b -= 1
            a -= 1
            distanceA = abs(a - userA[0]) + abs(b - userA[1])
            if distanceA <= c:
                possibleA.append([d, index])
            distanceB = abs(a - userB[0]) + abs(b - userB[1])
            if distanceB <= c:
                possibleB.append([d, index])
            index += 1

        #print(possibleA, possibleB)
        #if i > 0:
           # print(possibleA, possibleB)
           # print(amountA, amountB)

        if len(possibleA) > 0 and len(possibleB) == 0:
            amountA += possibleA[0][0]
            continue
        if len(possibleB) > 0 and len(possibleA) == 0:
            amountB += possibleB[0][0]
            continue
        if possibleB == possibleA and len(possibleB) == 1 and len(possibleA) == 1:
            amountA += int(possibleA[0][0] / 2)
            amountB += int(possibleB[0][0] / 2)
            continue
        if possibleB != possibleA and len(possibleB) == 1 and len(possibleA) == 1:
            amountA += int(possibleA[0][0])
            amountB += int(possibleB[0][0])
            continue
        if len(possibleA) >= 2 and len(possibleB) == 1:
            if possibleA[0] != possibleB[0]:
                amountA += possibleA[0][0]
                amountB += possibleB[0][0]
            else:
                amountA += possibleA[1][0]
                amountB += possibleB[0][0]
            continue
        if len(possibleB) >= 2 and len(possibleA) == 1:
            if possibleA[0][0] != possibleB[0][0]:
                amountA += possibleA[0][0]
                amountB += possibleB[0][0]
            if possibleA[0][0] == possibleB[0][0] and possibleA[0][1] == possibleB[0][1]:
                amountA += possibleA[0][0]
                amountB += possibleB[1][0]
            if possibleA[0][0] == possibleB[0][0] and possibleA[0][1] != possibleB[0][1]:
                amountA += possibleA[0][0]
                amountB += possibleB[0][0]
            continue
        if len(possibleB) >= 2 and len(possibleA) >= 2:
            #print("ASDFSAFDAFDS")
            if max(possibleA)[0] == max(possibleB)[0] and max(possibleA)[1] != max(possibleB)[1]:
                amountA += possibleA[0][0]
                amountB += possibleB[0][0]
                continue
            if max(possibleA)[0] == max(possibleB)[0] and max(possibleA)[1] == max(possibleB)[1]:
                if possibleA[1][0] >= possibleB[1][0]:
                    amountA += possibleA[1][0]
                    amountB += possibleB[0][0]
                else:
                    amountA += possibleA[0][0]
                    amountB += possibleB[1][0]
            if max(possibleA)[0] != max(possibleB)[0]:
                amountA += possibleA[0][0]
                amountB += possibleB[0][0]
                continue
    # print(" ")
    print("#" + str(t + 1) + " " + str(amountA + amountB))