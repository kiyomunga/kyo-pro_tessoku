#A10 Resort Hotel
N=int(input())
A=list(map(int,input().split()))
D=int(input())
L=[0]*D
R=[0]*D
for i in range(D):
    L[i],R[i]=map(int,input().split())
P=[0]*D
Q=[0]*D
for i in range(D):
    P[i]=A[:L[i]-1]
    Q[i]=A[R[i]:]
for i in range(D):
    for j in range(0,L[i]-3):
        P[i][j+1]=max(P[i][j+1],P[i][j])
for i in range(D):
    for j in range(N-R[i]-1):
        Q[i][j+1]=max(Q[i][j+1],Q[i][j])
for i in range(D):
    print(max(P[i][L[i]-2],Q[i][N-R[i]-1]))