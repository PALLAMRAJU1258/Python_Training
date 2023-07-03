def Fibonacci(n,dp):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif dp[n] != -1:
        return dp[n]
    else:
        dp[n] = Fibonacci(n-1,dp) + Fibonacci(n-2,dp)
        return dp[n]

num = int(input())
dp = [-1]*10
print(Fibonacci(num,dp))
print(dp)
print(Fibonacci(5,dp))
print(dp)