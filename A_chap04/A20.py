#A20 LCS
S="a"+input()
T="a"+input()
SL=len(S)
TL=len(T)
dp=[[0]*(TL+1)for i in range(SL+1)]
for i in range(0,TL+1):
    dp[0][i]=0

for i in range(1,SL):
    for j in range(1,TL):
        if S[i]==T[j]:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]+1)
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp[SL-1][TL-1])