def solution(n):
    answer = 0
    dp = [0] * (n+10)
    residue = 1234567
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    dp[4] = 5
    for i in range(5,n+1):
        dp[i]= dp[i-1] + dp[i-2]
        dp[i] = dp[i]%residue 
    answer = dp[n]
    return answer