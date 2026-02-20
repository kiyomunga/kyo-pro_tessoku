#A22 Sugoroke
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
dp=[None]*(N)
dp[0]=0
for i in range(0,N-1):
    if dp[i]!=None:
        if dp[A[i]-1]!=None:
            dp[A[i]-1]=max(dp[A[i]-1],dp[i]+100)
        else:
            dp[A[i]-1]=dp[i]+100
        if dp[B[i]-1]!=None:
            dp[B[i]-1]=max(dp[B[i]-1],dp[i]+150)
        else:
            dp[B[i]-1]=dp[i]+150

print(dp[N-1])