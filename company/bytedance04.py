n = 4
m = 876
v = [1,4,16,64]
f = [[0 for i in range(m+1)] for j in range(n)]
for i in range(n):
        f[i][0] = 1
for j in range(1, m+1):
        if j % v[0] == 0:
                dp[0][j] = 1
        else:
                dp[0][j] = 0
for i in range(1,n):
        for j in range(1, m+1):
                temp = 0
                for k in range(0,k*f[i]):
                        temp += dp[i-1]
                dp[i][j]=temp


