#A25 Number of Routes
H,W=map(int,input().split())
C=[0]*H
for i in range(H):
    C[i]=list(input().strip())

dp=[[0]*(W+1)for i in range(H+1)]
dp[1][0]=1
dp[0][1]=1

for i in range(1,H+1):
    for j in range(1, W+1):
        if C[i-1][j-1]==".":
            if i==1:
                dp[i][j]=dp[i][j-1]
            elif j==1:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i][j-1]+dp[i-1][j]
        else:
            dp[i][j]=0

print(dp[H][W])