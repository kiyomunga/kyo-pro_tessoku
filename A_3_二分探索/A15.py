#A15 Compression
N=int(input())
A=list(map(int,input().split()))
X=list(set(A))
X.sort()
B=[0]*N

for i in range(N):
    L=0
    R=len(X)-1
    while L<=R:
        M=(L+R)//2
        if A[i]>X[M]:
            L=M+1
        elif A[i]<X[M]:
            R=M-1
        else:
            L=R=M
            break
    B[i]=L+1
print(*B)
