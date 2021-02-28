import sys
input=sys.stdin.readline

#/3, /2, -1 => 1 #횟수 출력

n=int(input())
dp = [0 for _ in range(n + 1)]
print(dp)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
    print(dp)
print(dp[n])