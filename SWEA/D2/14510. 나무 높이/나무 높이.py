T = int(input().rstrip())

for t in range(1, T + 1):
    n = int(input().rstrip())
    data = list(map(int, input().split()))
    tall = max(data)
    days = 0

    while True:
        if len(set(data)) == 1:
            break
        data.sort()
        
        if days % 2 == 0:
            flag = 0
            for i in range(n-1, -1, -1):

                if data[i] + 1 == tall:
                    data[i] += 1
                    break

                if data[i] + 2 < tall:
                    data[i] += 1
                    break

                if data[i] + 2 == tall:
                    if flag == 1:
                        data[i] += 1
                        break
                    data[i] = data[i]
                    flag += 1

        if days % 2 == 1:
            for i in range(n):

                if data[i] + 2 == tall:
                    data[i] += 2
                    break

                if data[i] + 1 == tall:
                    data[i] = data[i]

                if data[i] + 2 < tall:
                    data[i] += 2
                    break
        days += 1
    print("#" + str(t) + " " + str(days))