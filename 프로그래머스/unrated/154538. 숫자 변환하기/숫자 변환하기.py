def solution(x, y, n):
    dp = [1000001] * (y+3)
    dp[x] = 0
    for i in range(x,y+1):
        if i+n<=y:
            dp[i+n] = min(dp[i+n],dp[i]+1)
        if i*2<=y:
            dp[i*2] = min(dp[2*i],dp[i]+1)
        if i*3<=y:
            dp[i*3] = min(dp[3*i],dp[i]+1)
    if dp[y] == 1000001:
        return -1
    return dp[y]