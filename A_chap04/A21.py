#A21 Block Game
N=int(input())
P=[0]*(N+1)
A=[0]*(N+1)
for i in range(1,N+1):
    P[i],A[i]=map(int,input().split())
dp=[[0]*(N+2)for i in range(N+2)]

for LEN in reversed(range(0,N-1)):
    for l in range(1,N-LEN+1):
        r=l+LEN
        if l>=2 and l<=P[l-1]<=r:
            score1=A[l-1]
        else:
            score1=0
        if r<=N-1 and l<=P[r+1]<=r:
            score2=A[r+1]
        else:
            score2=0
        if l==1:
            dp[l][r]=dp[l][r+1]+score2
        elif r==N:
            dp[l][r]=dp[l-1][r]+score1
        else:
            dp[l][r]=max(dp[l-1][r]+score1,dp[l][r+1]+score2)

M=[0]*(N+1)
for i in range(1,N+1):
    M[i]=dp[i][i]

print(max(M))